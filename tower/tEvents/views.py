from django.shortcuts import render, redirect
from .models import TEvent

# Create your views here.

def tEventsList(request):
    tEvents = TEvent.objects.all()
    return render(request, )