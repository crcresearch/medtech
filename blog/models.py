from django.conf import settings
from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=150,null=True)
    identification_card = models.IntegerField(null=True)
    specialty = models.CharField(max_length=150,null=True)
    phone = models.IntegerField(null=True)
    location = models.TextField(null=True)
    bio = models.TextField(null=True)
    EntranceHours=(
        (
            '7:00', '7:00'
        ),(
            '8:00', '8:00'
        ),(
            '9:00', '9:00'
        ),(
            '10:00', '10:00'
        ),(
            '11:00', '11:00'
        ),(
            '12:00', '12:00'
        ),(
            '13:00', '13:00'
        ),(
            '14:00', '14:00'
        ),(
            '15:00', '15:00'
        ),(
            '16:00', '16:00'
        ),(
            '17:00', '17:00'
        ),(
            '18:00', '18:00'
        ),(
            '19:00', '19:00'
        )
    )
    OutOfOffice=(
        (
            '7:00', '7:00'
        ),(
            '8:00', '8:00'
        ),(
            '9:00', '9:00'
        ),(
            '10:00', '10:00'
        ),(
            '11:00', '11:00'
        ),(
            '12:00', '12:00'
        ),(
            '13:00', '13:00'
        ),(
            '14:00', '14:00'
        ),(
            '15:00', '15:00'
        ),(
            '16:00', '16:00'
        ),(
            '17:00', '17:00'
        ),(
            '18:00', '18:00'
        ),(
            '19:00', '19:00'
        )
    )
    #CheckIn = models.CharField(max_length=100,choices=EntranceHours)
    #CheckOut=models.CharField(max_length=100,choices=OutOfOffice)



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
    name = models.CharField(max_length=150,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100,choices=genderOptions,null=True)
    place_of_birth = models.CharField(max_length=100,null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    mail = models.CharField(max_length = 100,null=True)
    phone = models.IntegerField(null=True)
    last_visit = models.TextField(null=True)
    alcohol = models.CharField(max_length=100, choices=yes_no,null=True)
    smoke = models.CharField(max_length=100, choices=yes_no,null=True)
    drugs = models.CharField(max_length=100, choices=yes_no,null=True)
    religion = models.CharField(max_length=255,null=True)
    allergies = models.CharField(max_length=100, choices=yes_no,null=True)
    last_diagnostic = models.TextField(null=True)
    meds = models.TextField(null=True)
