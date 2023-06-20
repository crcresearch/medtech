from django.shortcuts import render

# Create your views here.
def patient(request):
    return render(request, 'blog/patient.html', {})