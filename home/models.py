from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse 

class doctor(models.Model):
    username=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    phone=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    nid=models.CharField(max_length=1000)
    veri=models.CharField(max_length=1000,null=True)
    schedule_day=models.CharField(max_length=1000,null=True)
    schedule_time=models.CharField(max_length=1000,null=True)
    
    
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

class app(models.Model):
    username=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    doctor=models.CharField(max_length=1000)
    app_id=models.IntegerField()
    email=models.CharField(max_length=1000,null=True)
    
    
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name



