from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from tEvents.models import Ticket, TEvent
from . import forms

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = forms.myAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("tEvents:list")
    else:
        form = forms.myAuthenticationForm()
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = forms.myUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("tEvents:list")
    else:
        form = forms.myUserCreationForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("tEvents:list")
    
def accountPage(request):
    if request.user:
        tickets = Ticket.objects.filter(user=request.user.id)
    return render(request, "accountPage.html", {"tickets":tickets})

def deleteTicket(request, id):
    ticket = Ticket.objects.get(id=id)
    tEvent = TEvent.objects.get(id=ticket.tEvent.id)
    if ticket.user == request.user:
        ticket.delete()
        tEvent.capacity +=1
        tEvent.save()
    return redirect("users:account")