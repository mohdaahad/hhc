from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
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
    volunteers = Volunteers.objects.all()
    social_voluteers = Social_Voluteers.objects.all()
    paginator=Paginator(volunteers, 8)
    page_number =request.GET.get('page') 
    page_obj=paginator.get_page(page_number)
    return render(request, "account/volunteers.html",{'volunteers': page_obj,'social':social_voluteers})   


def donation_details(request):
    return render(request, "account/donation-details.html") 

def blog_details(request):
    return render(request, "account/blog-details.html")     

def gallery(request):
    # gallery = Gallery.objects.all()
    # paginator=Paginator(gallery, 8)
    # page_number =request.GET.get('page') 
    # page_obj=paginator.get_page(page_number)
    return render(request, "account/gallery.html") 

def my_ajax_view(request):
    data = Gallery.objects.all()
    paginator = Paginator(data, 8)
    page = request.GET.get('page')
    paginated_data = paginator.get_page(page)
    data_list = list(paginated_data.object_list.values())
    return JsonResponse({
        'data': data_list,
        'has_next': paginated_data.has_next(),
        'has_previous': paginated_data.has_previous(),
        'page':page,
        'previous_page_number': paginated_data.previous_page_number() if paginated_data.has_previous() else None,
        'next_page_number': paginated_data.next_page_number() if paginated_data.has_next() else None,
    })


def join_volunteers(request):
    return render(request, "account/join-volunteers.html") 

