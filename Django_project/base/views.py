from django.shortcuts import render

from base.models import Account, Income, Spends, Customer


def set_account_amount(account):
    incomes = Income.objects.filter(affected_account=account)
    spending = Spends.objects.filter(affected_account=account)
    amount = 0
    for inc in incomes:
        amount += inc.amount
    for spend in spending:
        amount -= spend.amount
    return amount


def home_page(request):
    account = Account.objects.get(id=1)
    incomes = Income.objects.filter(affected_account=account)
    spending = Spends.objects.filter(affected_account=account)
    account.amount = set_account_amount(account)
    context = {"account": account, "incomes": incomes, "spending": spending
               }
    return render(request, "home.html", context)


def family_page(request):
    # customer = Customer.objects.get(name="Kiril Kirilov")
    # account = Account.objects.filter(members=customer)[:1]
    account = Account.objects.get(name="Kirilovi")
    incomes = Income.objects.filter(affected_account=account)
    spending = Spends.objects.filter(affected_account=account)
    account.amount = set_account_amount(account)
    context = {"account": account, "incomes": incomes, "spending": spending
               }
    return render(request, "family.html", context)


def members_page(request):
    return render(request, "members.html")