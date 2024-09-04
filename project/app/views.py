from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def addcntct(req):
    if req.method=='POST':
        Name = req.POST['Name']
        Email = req.POST['Email']
        Phone = req.POST['Phone']
        Alternative = req.POST['Alternative']
        Image = req.FILES['Image']
        data=Contact.objects.create(Name=Name,Email=Email,Phone=Phone,Alternative=Alternative,Image=Image)
        data.save()
        return redirect(viewcntct)
    return render(req,'addcontact.html')

def viewcntct(req):
    data=Contact.objects.all()
    return render(req,'viewcntct.html',{'data':data})


def single(req,id):
    if 'contact' in req.session:
        data=Contact.objects.get(pk=id)
        return render(req,'singlecontact.html',{'data':data})
    else:
        return redirect(addcntct)
    
def edit(req,id):
    data=Contact.objects.get(pk=id)
    if req.method=='POST':
        Name = req.POST['Name']
        Email = req.POST['Email']
        Phone = req.POST['Phone']
        Alternative = req.POST['Alternative']
        
        Contact.objects.filter(pk=id).update(Name=Name,Email=Email,Phone=Phone,Alternative=Alternative)
        
        return redirect(viewcntct)
    return render(req,'edit.html',{'data':data})

def delete(req,id):
    data=Contact.objects.get(pk=id)
    data.delete()
    return redirect(viewcntct) 
