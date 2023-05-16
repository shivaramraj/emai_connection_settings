from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail

def Register(request):
    d={'UFO':UserForm(),'PFO':ProfileForm()}

    if request.method == 'POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid() :
            NSUFO=UFD.save(commit=False)
            NSUFO.set_password(UFD.cleaned_data['password'])
            NSUFO.save()
            NSPFO=PFD.save(commit=False)
            NSPFO.username=NSUFO
            NSPFO.save()
            send_mail(
                'registration',
                'registration sucessful',
                'shivaramraj5596@gmail.com',
                [NSUFO.email],
                fail_silently=False)
            return HttpResponse ('register is sucessfull')
        else:
            return HttpResponse('invalid data')



    return render(request,'Register.html',d)