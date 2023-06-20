from django.shortcuts import render,redirect
from .models import Patient


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


