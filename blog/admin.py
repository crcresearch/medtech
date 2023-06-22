from django.contrib import admin
from .models import Doctor,Patient,Diagnosis, Book

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Diagnosis)
admin.site.register(Book)

