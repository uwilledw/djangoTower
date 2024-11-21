from django.shortcuts import render, redirect
from .models import TEvent, Ticket, Comments
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
    attendees = Ticket.objects.filter(tEvent=tEvent)
    comments = Comments.objects.filter(eventId=id)
    if attendees.filter(user=request.user):
        isAttending = True
    else:
        isAttending = False
    form = forms.CreateComment()
    return render(request, 'tEventDetails.html', {'tEvent': tEvent, 'attendees':attendees, 'isAttending': isAttending, 'form': form, 'comments':comments})

@login_required(login_url="users/login")
def cancelEvent(request, id):
    tEvent = TEvent.objects.get(id=id)
    if request.user.id == tEvent.creator.id:
        tEvent.isCanceled = True
        tEvent.save()
    return redirect('tEvents:tEventDetails', id=tEvent.id)

@login_required(login_url="users/login")
def attendEvent(request, id):
    tEvent = TEvent.objects.get(id=id)
    tick = Ticket.objects.filter(tEvent=tEvent, user=request.user)
    if not tick and tEvent.capacity > 0:
        newTick = Ticket(tEvent=tEvent, user=request.user)
        tEvent.capacity -=1
        tEvent.save()
        newTick.save()
    return redirect('tEvents:tEventDetails', id=tEvent.id)

    

@login_required(login_url="users/login")
def createEvent(request):
    form = forms.CreateTEvent(request.POST, request.FILES)
    if form.is_valid():
        newEvent = form.save(commit=False)
        newEvent.creator = request.user
        newEvent.save()
        return redirect('tEvents:tEventDetails', id=newEvent.id)
    else:
        form = forms.CreateTEvent()
        return render(request, 'tEventForm.html', {'form': form})
    
@login_required(login_url="users/login")
def createComment(request, id):
    form = forms.CreateComment(request.POST, request.FILES)
    if form.is_valid():
        newComment = form.save(commit=False)
        newComment.creator = request.user
        newComment.eventId = id
        newComment.save()
    return redirect('tEvents:tEventDetails', id=id)

@login_required
def deleteComment(request, id, cId):
    comment = Comments.objects.get(id=cId)
    if comment.creator == request.user:
        comment.delete()
    return redirect('tEvents:tEventDetails', id=id)
