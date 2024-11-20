from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from tEvents.models import Ticket

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("tEvents:list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("tEvents:list")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("tEvents:list")
    
def accountPage(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, "accountPage.html", {"tickets":tickets})