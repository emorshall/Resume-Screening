from django.urls import path

from .views import home, register, signUpAction, loginAction, dashboard, resumeCategory

urlpatterns = [
    path("", home, name='home'),
    path("login.html", home, name='login'),
    path("register.html", register, name='register'),
    path("signUpAction", signUpAction),
    path("loginAction", loginAction),
    path("home.html", dashboard, name='dashboard'),
    path("tables.html", resumeCategory, name='category'),

]
