from django.shortcuts import render
from . forms import BookingForm

from .models import Departments,Doctors

# Create your views here.

def dep(request):
    dict_dep={
        'dep':Departments.objects.all()
    }
    return render(request,'deprtment.html',dict_dep) 


def doct(request):
    dict_docs={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def book(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confr.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)


def home(request):
    return render(request,'home.html') 
    
def about(request):
    return render(request,'about.html') 

# def book(request):
#     return render(request,'booking.html') 

# def doct(request):
#     return render(request,'doctors.html') 

# def dep(request):
#     return render(request,'deprtment.html') 

def cont(request):
    return render(request,'contact.html') 