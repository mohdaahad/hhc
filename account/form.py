from django.forms import ModelForm
from .models import Volunteers,Contacts
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import ClearableFileInput
class VolunteersForm(ModelForm):
    class Meta:
        model = Volunteers
        fields = ['full_name','father_name','email','education','country','region','city','pincode','phone','image',]
        labels ={'full_name':  'Full Name','father_name':'Father Name','email':'Email','phone':'Phone Number','education':'Education','country':'Country','region':'Region','city':'City'}
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'father_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your first name*'}),'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contry*'}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter your email*'}),'phone': PhoneNumberPrefixWidget(initial='IN',attrs={'placeholder':'Phone number.*', 'class': "form-control "}),'education':forms.Select(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'region':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your region*',}),'city':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your city*',}),'pincode':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter your pincode*',}) ,'image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder': 'Enter your image*','id':'file_input','multiple':True})}


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name','email','phone_number','subject','massage']
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter your email*'}),'phone_number':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter your phone number*',}),'subject':forms.TextInput(attrs={'class':'form-control','placeholder': 'Subject*',}),'massage':forms.Textarea(attrs={'class':'form-control','placeholder': 'Enter your Massage*',}),}

        