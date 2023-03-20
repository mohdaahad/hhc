from django.forms import ModelForm
from .models import Volunteers
from django import forms

class MyModelForm(ModelForm):
    class Meta:
        model = Volunteers
        fields = ['full_name','father_name','country','region','pincode','education','image','email','phone','city']
        labels ={'full_name':  'Full Name','father_name':'Father Name','email':'Email','phone':'Phone Number','education':'Education','country':'Country','region':'Region','city':'City'}
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your full name',}),'father_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your first name'}),'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Selecte Your Contry'}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email*'}), }