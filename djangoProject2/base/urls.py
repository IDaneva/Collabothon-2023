from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("family/", views.family_page, name="family"),
    path("members/", views.family_members, name="members")
]
