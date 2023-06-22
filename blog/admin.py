from django.contrib import admin
from .models import Doctor,Patient,Diagnosis

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Diagnosis)

