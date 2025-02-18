# Generated by Django 3.2.19 on 2023-06-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_patient_idd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='idd',
        ),
        migrations.AddField(
            model_name='doctor',
            name='identification_card',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='alcohol',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='drugs',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_visit',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='place_of_birth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='religion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='smoke',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
