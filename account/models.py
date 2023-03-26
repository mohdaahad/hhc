from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Gallery(models.Model): 
    image=models.ImageField(upload_to='static/account/image/gallery/') 
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)

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
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    education =models.CharField(max_length=32,choices=CHOICES ,default = 'Undergraduate',verbose_name="Choose your Education")
    image   =  models.ImageField(upload_to='static/account/image/volunteers/') 
    email = models.EmailField(max_length = 254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    visible_flag = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)

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
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.volunteers.full_name      



class Contacts(models.Model):
    name = models.CharField(max_length=100)    
    email = models.EmailField(max_length = 254)
    phone_number = PhoneNumberField(null=False, blank=False)
    subject = models.CharField(max_length=300) 
    massage = models.TextField(max_length=300) 
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    

    def __str__(self):
        return self.name   



class Feature_Campaigns(models.Model):
    tag = models.CharField(max_length=100)    
    title = models.CharField(max_length=300) 
    description = models.TextField(max_length=300) 
    image   =  models.ImageField(upload_to='static/account/image/featured/') 
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    


    def __str__(self):
        return self.tag   


class Donation(models.Model):
    campaigns = models.ForeignKey(Feature_Campaigns, default = 'Education',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length = 254)  
    phone_number = PhoneNumberField(null=False, blank=False)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField() 
    amount = models.IntegerField() 
    reference = models.IntegerField(null=True,default=0) 
    Certificate_80G = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    


    def __str__(self):
        return self.name                   