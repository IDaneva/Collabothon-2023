from django.shortcuts import render

from base.models import Account, Income, Spends


def home_page(request):
    account = Account.objects.get(id=1)
    incomes = Income.objects.filter(affected_account=account)
    spending = Spends.objects.filter(affected_account=account)
    amount = 0
    for inc in incomes:
        amount += inc.amount
    for spend in spending:
        amount -= spend.amount
    account.amount = amount
    context = {"account": account, "incomes": incomes, "spending": spending
               }
    return render(request, "home.html", context)


def family_page(request):
    return render(request, "family.html")


def members_page(request):
    return render(request, "members.html")