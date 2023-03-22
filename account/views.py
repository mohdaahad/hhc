from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from .form import *
# Create your views here.
#  dir_list = os.listdir("/home/mohdaahad/Documents/HHC_v1/src/hhc/static/account/image/gallery")
#     random.shuffle(dir_list)
def home(request):
    return render(request, "account/home.html")

def about(request):
    return render(request, "account/about.html")    

def contact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST) 
        if form.is_valid():
            form.save()
            return JsonResponse({'success': "successful submit your form"})
        # else:
        #     # errors = {}
        #     # for field in form.errors:
        #     #     errors[field] = form.errors[field][0]
        #     # print(errors)      
        #     return JsonResponse({'errors': errors})
    else:
        form = ContactsForm()
    return render(request, "account/contact.html",{'form': form})     

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

def volunteers_ajax(request):
    volunteers = Volunteers.objects.all()
    social_voluteers = list(Social_Voluteers.objects.values())
    paginator=Paginator(volunteers, 8)
    page_number =request.GET.get('page') 
    paginated_data=paginator.get_page(page_number)
    data_list = list(paginated_data.object_list.values())
    return JsonResponse({
        'data': data_list,
        'has_next': paginated_data.has_next(),
        'has_previous': paginated_data.has_previous(),
        'page':page_number,
        'social_voluteers':social_voluteers,
        'previous_page_number': paginated_data.previous_page_number() if paginated_data.has_previous() else None,
        'next_page_number': paginated_data.next_page_number() if paginated_data.has_next() else None,
    })
def donation_details(request):
    return render(request, "account/donation-details.html") 

def blog_details(request):
    return render(request, "account/blog-details.html")     

def gallery(request):
    return render(request, "account/gallery.html") 

def gallery_ajax(request):
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
    if request.method == 'POST':
        form = VolunteersForm(request.POST,request.FILES)   
        if form.is_valid():
            form.save()
            return JsonResponse({'success': "successful submit your form"})
        else:
            errors = {}
            for field in form.errors:
                errors[field] = form.errors[field][0]
            print(errors)      
            return JsonResponse({'errors': errors})
    else:
        form = VolunteersForm()
    return render(request, "account/join-volunteers.html",{'form': form}) 

