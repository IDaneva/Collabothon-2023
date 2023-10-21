from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("family/", views.family_page, name="family"),
    path("members/", views.family_members, name="members"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_user, name="register"),

]
