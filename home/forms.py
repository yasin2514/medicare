from django import forms
from django.contrib.auth.forms import UserChangeForm
from.models import doctor



class edit_profile_form(forms.ModelForm):

    schedule_day=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    schedule_time=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    

    class Meta:
        model = doctor
        fields = ('schedule_day','schedule_time')


 