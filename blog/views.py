from django.shortcuts import render,redirect
from .models import Patient, Doctor, Diagnosis

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
            return redirect('blog/doctor.html', pk=post.pk)
    else:
        doctors = Doctor.objects.all()
        doctor = doctors.first()
        form = Doctor()
        groups = []
        for group in request.user.groups:
            groups.append(group.name)
        return render(request, 'blog/doctor.html',{'doctor':doctor,'groups':group})

def diagnosis(request):
    if request.method == "POST":
        form = Diagnosis(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.name
            post.save()
            print(Diagnosis.objects.all())
            return redirect('blog/diagnosis.html', pk=post.pk)
    else:
        diagnoses = Diagnosis.objects.all()
        diagnosis = diagnoses.first()
        form = Diagnosis()
        return render(request, 'blog/diagnosis.html',{'diagnosis':diagnosis})