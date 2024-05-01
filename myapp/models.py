from django.db import models

# Create your models here.

class Imeage(models.Model):
    photo =models.ImageField(upload_to="myimeage")
    date =models.DateTimeField(auto_now_add=True)

class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    websitelink=models.CharField(max_length=70)
    message=models.TextField()

class Member(models.Model):
    Fname =models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Fathername= models.CharField(max_length=50)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=15)
    Country=models.CharField(max_length=50)
    Education=models.CharField(max_length=50)
    Bank_ac=models.CharField(max_length=50)
    himalay=models.CharField(max_length=50)
    man=models.CharField(max_length=50)
    h=models.CharField(max_length=50,default="Date")
    m=models.CharField(max_length=50,default="day")

