from django.conf import settings
from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=150)
    identification_card = models.IntegerField(max_length=200)
    specialty = models.CharField(max_length=150)
    phone = models.IntegerField
    location = models.TextField()
    bio = models.TextField()


class Patient(models.Model):
    genderOptions = (
        (
            'Male',
            'Male',
        ),
        (
            'Female',
            'Female',
        ),
        (
            'Prefer not to say',
            'Prefer not to say',
        ),

    )
    yes_no = (
        (
            'No',
            'No',
        ),
        (
            'Yes',
            'Yes'
        )
    )
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=100,choices=genderOptions)
    place_of_birth = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    mail = models.CharField(max_length = 100)
    phone = models.IntegerField()
    last_visit = models.TextField()
    alcohol = models.CharField(max_length=100, choices=yes_no)
    smoke = models.CharField(max_length=100, choices=yes_no)
    drugs = models.CharField(max_length=100, choices=yes_no)
    religion = models.CharField(max_length=255)
    allergies = models.CharField(max_length=100, choices=yes_no)
