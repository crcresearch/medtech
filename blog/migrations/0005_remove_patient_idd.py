# Generated by Django 3.2.19 on 2023-06-19 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_placeofbirth_patient_place_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='idd',
        ),
    ]
