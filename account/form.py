from django.forms import ModelForm
from .models import Volunteers
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import ClearableFileInput
class MyModelForm(ModelForm):
    class Meta:
        model = Volunteers
        fields = ['full_name','father_name','email','education','country','region','city','pincode','phone','image',]
        labels ={'full_name':  'Full Name','father_name':'Father Name','email':'Email','phone':'Phone Number','education':'Education','country':'Country','region':'Region','city':'City'}
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your full name*',}),'father_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your first name*'}),'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your contry*'}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter the your email*'}),'phone': PhoneNumberPrefixWidget(initial='IN',attrs={'placeholder':'Phone number.*', 'class': "form-control "}),'education':forms.Select(attrs={'class':'form-control','placeholder': 'Enter the your full name*',}),'region':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your region*',}),'city':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the your city*',}),'pincode':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter the your pincode*',}) ,'image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder': 'Enter the your image*','id':'file_input','multiple':True})}