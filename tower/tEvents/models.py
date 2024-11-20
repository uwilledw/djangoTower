from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TEvent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    coverImg = models.CharField(max_length=1000, verbose_name='Cover Image')
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()
    startDate = models.DateTimeField(verbose_name="Start Date")
    isCanceled = models.BooleanField(default=False, verbose_name="Is Canceled")
    EventType = models.TextChoices("EventType", "concert convention sport digital")
    type = models.CharField(blank=True, choices=EventType.choices, max_length=10)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    isPremium = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tEvent = models.ForeignKey(TEvent, on_delete=models.CASCADE)


class Comments(models.Model):
    body = models.TextField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    eventId = models.IntegerField()
