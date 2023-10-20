from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def family_page(request):
    return render(request, "family.html")


def members_page(request):
    return render(request, "members.html")