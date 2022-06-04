from django.contrib.messages.api import success
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import doctor
from .forms import edit_profile_form
from .models import app


class home(ListView):
    model=doctor
    template_name = 'medicare.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')

class form(ListView):
    model=doctor
    template_name = 'form.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')

def be_doctor(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        nid=request.POST['nid']
        veri=request.POST['veri']
        if doctor.objects.filter(username=username,veri="verified").exists():
            messages.error(request,'You are already a doctor')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if doctor.objects.filter(username=username,veri="not_verify").exists():
            messages.error(request,'Your request is under review')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            doctor_model=doctor(username=username,name=name,phone=phone,address=address,nid=nid,veri=veri)
            doctor_model.save()
            messages.success(request,'Your request is submitted')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'registration.html')


def signout(request):
    logout(request)
    return redirect("/")

class doctor_list (ListView):
    model = doctor
    template_name = "doctor_list.html"

class doctor_profile (DetailView):
    model = doctor
    template_name = "doctor_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(doctor_profile, self).get_context_data(*args, **kwargs)
        context['app_list'] = app.objects.all()
        return context

class profile (DetailView):
    model = doctor
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['app_list'] = app.objects.all()
        return context

class edit (UpdateView):
    model = doctor
    form_class = edit_profile_form
    template_name = "edit.html"

def app_form(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        doctor=request.POST['doctor']
        app_id=request.POST['app_id']
        email=request.POST['email']
        if app.objects.filter(username=username).exists():
            messages.error(request,'You have already requested')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            app_database=app(username=username,name=name,doctor=doctor,app_id=app_id,email=email)
            app_database.save()
            messages.success(request,'Your request is submitted')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
