from django.shortcuts import render, redirect
from .models import TEvent
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def tEventsList(request, type=None):
    if type:
        tEvents = TEvent.objects.filter(type=type)
    else:
        tEvents = TEvent.objects.all()
    return render(request, 'tEventsList.html', {'tEvents': tEvents})

def tEventDetails(request, id):
    tEvent = TEvent.objects.get(id=id)
    return render(request, 'tEventDetails.html', {'tEvent': tEvent})

@login_required(login_url="users/login")
def createEvent(request):
    form = forms.CreateTEvent(request.POST, request.FILES)
    if form.is_valid():
        newEvent = form.save(commit=False)
        newEvent.creator = request.user
        newEvent.save()
        return redirect('tEvents:list')
    else:
        form = forms.CreateTEvent()
        return render(request, 'tEventForm.html', {'form': form})