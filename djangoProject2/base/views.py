from django.shortcuts import render
from base.models import Account, Customer, Transactions
from django.db.models import Q


def set_account_amount(account):
    transactions = Transactions.objects.filter(affected_account=account)
    amount = 0
    for t in transactions:
        amount += t.amount
    return amount


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
        person__name__icontains=q,
        affected_account=account
    )
    # customer = Customer.objects.get(name="Kiril Kirilov")
    # account = Account.objects.filter(members=customer)[:1]
    # transactions = Transactions.objects.filter(affected_account=account)
    account.amount = set_account_amount(account)
    members = account.members
    context = {"account": account,
               "transactions": transactions,
               "members": members,
               # "transactions_i": transactions_i
               }
    return render(request, "family.html", context)


def members_page(request):
    return render(request, "members.html")
