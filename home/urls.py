from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include





urlpatterns = [
   
    path('',views.home.as_view(),name='home'),
    path('signin',views.signinn,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('form/',views.form.as_view(),name="form"),
    path('be_doctor/',views.be_doctor,name="be_doctor"),
    path('doctor_list/',views.doctor_list.as_view(),name="doctor_list"),
    path('doctor_profile/<int:pk>',views.doctor_profile.as_view(),name="doctor_profile"),
    path('profile/<int:pk>',views.profile.as_view(),name="profile"),
    path('edit/<int:pk>',views.edit.as_view(),name="edit"),
    path('app_form/',views.app_form,name="app_form"),

]