from django.forms import ModelForm
from .models import Volunteers,Contacts,Donation
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import ClearableFileInput
from django import forms
class VolunteersForm(ModelForm):
    class Meta:
        model = Volunteers
        fields = ['full_name','father_name','email','education','country','region','city','pincode','phone','image',]
        labels ={'full_name':  'Full Name','father_name':'Father Name','email':'Email','phone':'Phone Number','education':'Education','country':'Country','region':'Region','city':'City'}
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'father_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your father name*'}),'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contry*'}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter your email*'}),'phone': PhoneNumberPrefixWidget(initial='IN',attrs={'placeholder':'Phone number.*', 'class': "form-control "}),'education':forms.Select(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'region':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your state*',}),'city':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your city*',}),'pincode':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter your pincode*',}) ,'image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder': 'Enter your image*','id':'file_input'})}


class DonationForm(ModelForm):
    class Meta:
        model = Donation
       
        fields = ['campaigns','name','email','phone_number','country','region','city','pincode','amount','reference','Certificate_80G','pan_card']
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'pan_card':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your pan card number*',}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter your email*'}),'phone_number':PhoneNumberPrefixWidget(initial='IN',attrs={'class':'form-control','placeholder': 'Enter your phone number*',}),'country':forms.TextInput(attrs={'class':'form-control','placeholder': 'Country*',}),'region':forms.TextInput(attrs={'class':'form-control','placeholder': 'State*',}),'city':forms.TextInput(attrs={'class':'form-control','placeholder': 'City*',}),'pincode':forms.NumberInput(attrs={'class':'form-control','placeholder': 'PinCode*',}),'amount':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Amount INR*',}),'reference':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Ref code',}),'Certificate_80G':forms.CheckboxInput(attrs={'class':'switch_1',}),}

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name','email','phone_number','subject','massage']
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name*',}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter your email*'}),'phone_number':PhoneNumberPrefixWidget(initial='IN',attrs={'class':'form-control','placeholder': 'Enter your phone number*',}),'subject':forms.TextInput(attrs={'class':'form-control','placeholder': 'Subject*',}),'massage':forms.Textarea(attrs={'class':'form-control','placeholder': 'Enter your Massage*',}),}
        