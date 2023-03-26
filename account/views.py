from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from .form import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#  dir_list = os.listdir("/home/mohdaahad/Documents/HHC_v1/src/hhc/static/account/image/gallery")
#     random.shuffle(dir_list)
def home(request):
    campaigns = Feature_Campaigns.objects.all()
    return render(request, "account/home.html",{'campaigns':campaigns})

def about(request):
    return render(request, "account/about.html")    

def contact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST) 
        if form.is_valid():
            form.save()
            return JsonResponse({'success': "Successful submit your Massage"})
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
    if request.method == 'POST':
        form = DonationForm(request.POST)   
        if form.is_valid():
            form.save()
    #         param_dict={
    #         'MID': 'WorldP64425807474247',
    #         'ORDER_ID': str(form.id),
    #         'TXN_AMOUNT': '1',
    #         'CUST_ID': str(form.email),
    #         'INDUSTRY_TYPE_ID': 'Retail',
    #         'WEBSITE': 'WEBSTAGING',
    #         'CHANNEL_ID': 'WEB',
    #         'CALLBACK_URL':'http://127.0.0.1:8000/donation-details/',

    # }
            return JsonResponse({'success': "Successful donate"})
        else:
            errors = {}
            for field in form.errors:
                errors[field] = form.errors[field][0]      
            return JsonResponse({'errors': errors})
    else:
        form = DonationForm()
    return render(request, "account/donation-details.html",{'form':form}) 

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
            return JsonResponse({'success': "Successful submit your form"})
        else:
            errors = {}
            for field in form.errors:
                errors[field] = form.errors[field][0]
            print(errors)      
            return JsonResponse({'errors': errors})
    else:
        form = VolunteersForm()
    return render(request, "account/join-volunteers.html",{'form': form}) 

@csrf_exempt
def handlerequest(request):
    return  JsonResponse()