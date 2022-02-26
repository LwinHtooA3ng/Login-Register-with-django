from django.shortcuts import redirect, render

from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "accounts/index.html", {})

def registerUser(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {'form': form})

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or Password is invalid !")
        else:
            messages.error(request, "Fill out all the fields.")

    return render(request, "accounts/login.html", {})

@login_required
def home(request):
    return render(request, "accounts/home.html", {})

def logoutUser(request):
    logout(request)
    return redirect("index")