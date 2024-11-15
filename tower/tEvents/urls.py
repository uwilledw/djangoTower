from django.urls import path
from . import views

app_name = 'tEvents'

urlpatterns = [
    path('', views.tEventsList, name="list"),
    # path('<id:id>', views.tEventPage, name="tEventDetails")
    path('new-tEvent/', views.createEvent, name="newEvent")
]
