from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import Login


# Create your views here.
def dashboard(request):
    return render(request, "home.html", {})


def home(request):
    return render(request, "login.html", {"message": "Login"})


def register(request):
    return render(request, "register.html", {})


def resumeCategory(request):
    return render(request, "tables.html", {})


def signUpAction(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # getLoginTable = Login.get_latest_by()
            print(f'get username: ' + form.cleaned_data['name'])
            print(f'get password: ' + form.cleaned_data['password'])
            return redirect('login')
        else:
            form = LoginForm()
            return render(request, 'register.html', {})


def loginAction(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['name']
        password = form.cleaned_data['password']
        if validateUser(username, password):
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {"message": "Invalid User ! Please Retry"})


def validateUser(username, password):
    validate = False
    getLoginTable = Login.objects.all()
    for val in getLoginTable:
        if (username == val.name) & (password == val.password):
            validate = True
            break
    return validate
