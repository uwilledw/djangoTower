from django import forms
from . import models

class CreateTEvent(forms.ModelForm):
    class Meta:
        model = models.TEvent
        fields = ['name', 'description', 'coverImg', 'location', 'capacity', 'startDate', 'isCanceled', 'type']
        widgets = {
            "startDate": forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }