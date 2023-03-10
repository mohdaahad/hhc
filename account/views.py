from django.shortcuts import render
import os 
import random

volunteers={
    'VAJID MALIK':'vajidmalik.png',
    'MO KADIR':'mokadir.png',
    'ASHU QURESHI':3,
    'MO SHADAB':4,
    'PRAVEZ ALAM':5,
    'ARSHAD MALIK':6,
    'MEHFOOZ MALIK':7,
    'MO SHAHZAD':8,
    'AHSAN MALIK':9,
    'MO AAMIR':10,
    'MUSTAKEEM MALIK':11,
    'MO SHADAB':12,
}

# Create your views here.

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
    dir_list = os.listdir("/home/mohdaahad/Documents/HHC_v1/src/hhc/static/account/image/gallery")
    random.shuffle(dir_list)
    return render(request, "account/gallery.html",{'photo': dir_list})      


def join_volunteers(request):
    return render(request, "account/join-volunteers.html") 

