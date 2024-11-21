from django import forms
from . import models

class CreateTEvent(forms.ModelForm):
    class Meta:
        model = models.TEvent
        fields = ['name', 'description', 'coverImg', 'location', 'capacity', 'startDate', 'type']
        widgets = {
            "startDate": forms.DateTimeInput(attrs={'type': 'datetime-local', 'class':'form-control mt-2'}),
            "name": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "description": forms.Textarea(attrs={'class': 'form-control mt-2'}),
            "coverImg": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "location": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "capacity": forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            "type": forms.Select(attrs={'class': 'form-select mt-2'})
        }

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['body']
        widgets= {
            "body": forms.Textarea(attrs={'class': 'form-control mt-2', 'rows':3})
        }