from django.shortcuts import render, redirect

from base.models import Account, Customer, Transactions

from django.db.models import Count

from django.db.models import Q

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth.models import User


def set_account_amount(account):
    transactions = Transactions.objects.filter(affected_account=account)
    amount = 0
    for t in transactions:
        amount += t.amount
    return amount


def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, "Incorrect password")

        else:
            login(request, user)
            return redirect("home")

    context = {"page": page}
    return render(request, "login_register.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")


def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred. Try again")

    context = {"form": form}
    return render(request, "login_register.html", context)


def home_page(request):
    account = Account.objects.get(id=1)
    transactions = Transactions.objects.filter(affected_account=account)
    account.amount = set_account_amount(account)
    context = {"account": account, "transactions": transactions
               }
    return render(request, "home.html", context)


def family_page(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    account = Account.objects.get(name="Kirilovi")

    transactions = Transactions.objects.filter(
        (Q(person__name__icontains=q) & Q(affected_account=account)) |
        (Q(affected_account=account) & Q(category__icontains=q))
    )

    total_spent_amount = sum(t.amount for t in transactions if t.amount < 0)
    total_income_amount = sum(t.amount for t in transactions if t.amount >= 0)

    category_counts = Transactions.objects.values('category').annotate(count=Count('category'))
    unique_categories = [item['category'] for item in category_counts]

    # customer = Customer.objects.get(name="Kiril Kirilov")
    # account = Account.objects.filter(members=customer)[:1]
    # transactions = Transactions.objects.filter(affected_account=account)
    account.amount = set_account_amount(account)
    members = account.members
    context = {"account": account,
               "transactions": transactions,
               "members": members,
               "categories": unique_categories,
               "total_spent_amount": total_spent_amount,
               "total_income_amount": total_income_amount
               }
    return render(request, "family.html", context)


def family_members(request):
    account = Account.objects.get(name="Kirilovi")
    account.amount = set_account_amount(account)
    member_accounts = []
    for m in account.members.all():
        current_account = Account.objects.get(name=m.name)
        if current_account.number != account.number:
            member_accounts.append(current_account)
    context = {"account": account, "member_accounts": member_accounts}
    return render(request, "members.html", context)

