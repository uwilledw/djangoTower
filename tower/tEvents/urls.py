from django.urls import path
from . import views

app_name = 'tEvents'

urlpatterns = [
    path('', views.tEventsList, name="list"),
    path('<str:type>', views.tEventsList, name="list"),
    path('tEvents/<int:id>', views.tEventDetails, name="tEventDetails"),
    path('tEvents/<int:id>/cancel', views.cancelEvent, name="cancel"),
    path('tEvents/<int:id>/attend', views.attendEvent, name="attend"),
    path('new-tEvent/', views.createEvent, name="newEvent")
]
