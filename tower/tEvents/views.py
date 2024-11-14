from django.shortcuts import render, redirect
from .models import TEvent

# Create your views here.

def tEventsList(request):
    tEvents = TEvent.objects.all()
    return render(request, 'tEventsList.html', {'tEvents': tEvents})

def tEventDetails(request, id):
    tEvent = TEvent.objects.get(id=id)
    return render(request, 'tEventDetails.html', {'tEvent': tEvent})