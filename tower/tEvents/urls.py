from django.urls import path
from . import views

app_name = 'tEvents'

urlpatterns = [
    path('', views.tEventsList, name="list")
]
