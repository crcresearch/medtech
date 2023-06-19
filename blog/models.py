from django.conf import settings
from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    idd = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #dates = ...
    #appointments = 
    bio = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)


class Patient(models.Model):
    genderOptions = (
        (
            'Male',
            'Male',
        ),

    )
    placeOfBirth = (

    )
    height = models.IntegerField()
    weight = models.IntegerField()
    mail = models.CharField(max_length = 100)
    
    idd = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=100,choices=genderOptions)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

