from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe
class Gallery(models.Model): 
    title = models.CharField(max_length=300)
    image=models.ImageField(upload_to='static/account/image/gallery/') 
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)
    def image_tag(self):
            return mark_safe('<img src="/%s" width="100"  />' % (self.image))

    image_tag.short_description = 'Image'
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
    id = models.AutoField(primary_key=True)
    campaigns = models.ForeignKey(Feature_Campaigns, default = 'Education',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length = 254)  
    phone_number = PhoneNumberField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField() 
    amount = models.IntegerField() 
    reference = models.IntegerField(null=True,default=0) 
    pan_card = models.CharField(max_length=100)  
    pay_id = models.CharField(max_length=200,blank=True)  
    Certificate_80G = models.BooleanField(default=False)
    pay_status = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    


    def __str__(self):
        return self.name                   
    

class Donations(models.Model):
    COLOR_CHOICES = (
    ('Cash','Cash'),
    ('UPI', 'UPI'),
    ('Cheque','Cheque'),
    ('Net Banking','Net Banking'),

)
    id = models.AutoField(primary_key=True)
    campaigns = models.ForeignKey(Feature_Campaigns, default = 'Education',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length = 254)  
    phone_number = PhoneNumberField()
    amount = models.IntegerField() 
    pan_card = models.CharField(max_length=100)  
    pay_mode = models.CharField(max_length=11, choices=COLOR_CHOICES, default='UPI')
    pay_id = models.CharField(max_length=200,blank=True)  
    Certificate_80G = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    


    def __str__(self):
        return self.name                   
class Certificate_80g(models.Model):
    donater = models.OneToOneField(Donations, on_delete=models.CASCADE)
    Certificate_80G_no = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='static/account/pdf/')
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    updated_date =models.DateTimeField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)    


    def __str__(self):
        return self.Certificate_80G_no          


class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200) 
