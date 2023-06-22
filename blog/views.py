from django.shortcuts import render,redirect
from .models import Patient
from .models import Doctor
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login



def patient(request):
    if request.method == "POST":
        form = Patient(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.name
            post.save()
            print(Patient.objects.all())
            #return render(request, 'blog/patient.html', {})
            return redirect('blog/patient.html', pk=post.pk)
    else:
        #print(Patient.objects.all())
        patients = Patient.objects.all()
        patient = patients.first()
        form = Patient()
        return render(request, 'blog/patient.html',{'patient':patient})


def doctor(request):
    if request.method == "POST":
        form = Doctor(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.name
            post.save()
            print(Doctor.objects.all())
            #return render(request, 'blog/patient.html', {})
            return redirect('blog/doctor.html', pk=post.pk)
    else:
        #print(Patient.objects.all())
        doctors = Doctor.objects.all()
        doctor = doctors.first()
        form = Doctor()
        groups = []
        for group in request.user.groups:
            groups.append(group.name)
        return render(request, 'blog/doctor.html',{'doctor':doctor,'groups':group})


def login_view(request):
    
    if request.method == 'POST':
        login(request, user)
        username = request.POST["username"]
        password = request.POST["password"]
        # Redirect to a success page.
        user = authenticate(request, username=username, password=password)

    else:
        # Return an 'invalid login' error message.
        print('Invalid login')

def logout_view(request):
    logout(request)

