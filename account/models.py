from django.db import models

# Create your models here.
class Gallery(models.Model): 
    image=models.ImageField(upload_to='static/account/image/gallery/') 
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
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
    address = models.CharField(max_length=100)
    eduction =models.CharField(max_length=32,choices=CHOICES,default='Undergraduate' ,verbose_name="Chuse your Eduction")
    image   =  models.ImageField(upload_to='static/account/image/gallery/') 
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=20)
    visible_flag = models.BooleanField(default=False)
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
    Created_by = models.TextField(max_length=200,blank=True)
    updated_by = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.full_name    