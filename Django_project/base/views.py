from django.shortcuts import render

from base.models import Account


def home_page(request):
    account = Account.objects.get(id=1)
    context = {"account": account
               }
    return render(request, "home.html", context)


def family_page(request):
    return render(request, "family.html")


def members_page(request):
    return render(request, "members.html")