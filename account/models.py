from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cities.models import City, Country, Region
# Create your models here.
class Gallery(models.Model): 
    image=models.ImageField(upload_to='static/account/image/gallery/') 
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.TextField(max_length=200,blank=True)
    updated_by = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.image.url


class Volunteers(models.Model): 
    CHOICES=[
        ('undergraduate ','Undergraduate '),
        ('postgraduate','Postgraduate'),
        ('other','Other'),
       ]
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    education =models.CharField(max_length=32,choices=CHOICES,default='Undergraduate' ,verbose_name="Choose your Education")
    image   =  models.ImageField(upload_to='static/account/image/volunteers/') 
    email = models.EmailField(max_length = 254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    visible_flag = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.TextField(max_length=200,blank=True)
    updated_by = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.full_name    


class Social_Voluteers(models.Model):
    CHOICES=[
        ('fa-facebook-f ','Facebook '),
        ('fa-instagram','Instagram'),
        ('fa-linkedin-in','LinkedIn'),
        ('fa-twitter','Twitter'),
       ]
    volunteers = models.ForeignKey(Volunteers, on_delete=models.CASCADE)
    account =models.CharField(max_length=32,choices=CHOICES,default='Facebook' ,verbose_name="Choose your social media account")
    url = models.URLField(max_length=300)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.TextField(max_length=200,blank=True)
    updated_by = models.TextField(max_length=200,blank=True)


    def __str__(self):
        return self.volunteers.full_name      