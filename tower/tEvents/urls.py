from django.urls import path
from . import views

app_name = 'tEvents'

urlpatterns = [
    path('', views.tEventsList, name="list"),
    path('<str:type>', views.tEventsList, name="list"),
    path('<int:id>', views.tEventDetails, name="tEventDetails"),
    path('new-tEvent/', views.createEvent, name="newEvent")
]
