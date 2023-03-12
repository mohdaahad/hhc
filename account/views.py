from django.shortcuts import render
import os 
import random
from .models import  Gallery
from django.core.paginator import Paginator
# Create your views here.
#  dir_list = os.listdir("/home/mohdaahad/Documents/HHC_v1/src/hhc/static/account/image/gallery")
#     random.shuffle(dir_list)
def home(request):
    return render(request, "account/home.html")

def about(request):
    return render(request, "account/about.html")    

def contact(request):
    return render(request, "account/contact.html")     

def donation_listing(request):
    return render(request, "account/donation-listing.html")    

def blog(request):
    return render(request, "account/blog.html")      


def events(request):
    return render(request, "account/events.html")      

def faq(request):
    return render(request, "account/faq.html") 

def service(request):
    return render(request, "account/service.html")   

def volunteers(request):
    return render(request, "account/volunteers.html")   


def donation_details(request):
    return render(request, "account/donation-details.html") 

def blog_details(request):
    return render(request, "account/blog-details.html")     

def gallery(request):
    gallery = Gallery.objects.all()
    paginator=Paginator(gallery, 8)
    page_number =request.GET.get('page') 
    page_obj=paginator.get_page(page_number)
    return render(request, "account/gallery.html",{'photo': page_obj})      


def join_volunteers(request):
    return render(request, "account/join-volunteers.html") 

