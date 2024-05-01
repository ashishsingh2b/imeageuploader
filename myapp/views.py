from django.shortcuts import render
from .forms import ImeageFrom
from .models import Imeage
from .models import contactEnquiry
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.method=='POST':
        form = ImeageFrom(request.POST,request.FILES)
        if form.is_valid():
         form.save()
    form=ImeageFrom()
    img =Imeage.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})

def contact(request):
   return render(request,'myapp/form.html')

def saveEnquary(request):
   if request.method=="POST":
      name=request.POST.get('Name')
      email=request.POST.get('Email')
      phone=request.POST.get('Phone')
      website=request.POST.get('Wesbiste')
      message=request.POST.get('Message')
      en=contactEnquiry(name=name,email=email,phone=phone,websitelink=website,messgae=message)
      en.save()
   return render(request,'myapp/form.html')


