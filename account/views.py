from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from .form import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .chacksum import generate_checksum, verify_checksum
from django.core.mail import EmailMessage,BadHeaderError    
import pdfkit
from django.http import HttpResponse
import os
from django.template.loader import render_to_string
from datetime import datetime,date
# Create your views here.

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


def generate_pdf(name,cert_id,amount,pay_id,phone_no,pan_card,email):
    context = {'name': name, 'no':cert_id,'date':date.today().strftime("%d-%m-%Y"),'amount':amount,'id':pay_id,'pan_card_no':pan_card,'gmail':email,'phone_no':phone_no}
    html_template = 'account/my.html'
    rendered_html = render_to_string(html_template, context)
    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static/account/pdf', f"{cert_id}.pdf")
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pdf = pdfkit.from_string(rendered_html, output_path)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=f"{i}.pdf"'
    return output_path

def sendMail(name,cert_id,amount,pay_id,email,phone_no,pan_card):
    pdf = generate_pdf(name,cert_id,amount,pay_id,phone_no,pan_card,email)
    date1= date.today().strftime("%d-%m-%Y")
    subject = "Donation Receipt for Your Generous Contribution to Helping Hands Community"
    message = f"""Dear {name},
We would like to express our sincere gratitude for your recent donation to Helping Hands Community. Your generous contribution will make a significant difference in our efforts to support those in need and make a positive impact in our community.

We have processed your donation and are pleased to provide you with the following receipt for your records:

Donation Amount: {amount}
Date of Donation: {date1}
Donation Type: UPI

We are a non-profit organization and all donations are tax-deductible as allowed by law. Please consult with your tax advisor for any specific tax-related questions.

Thank you again for your kindness and support. We could not do what we do without the help of donors like you.

Best regards,

Afzal Ahamad
Helping Hands Community"""
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    mail.attach_file(pdf)
    try:
      mail.send()
    except BadHeaderError as e:
        print("Email not sent. Invalid header:", e)
    except Exception as e:
        print("Email not sent. An error occurred:", e)
    return pdf

   
def donation_details(request):
    if request.method == 'POST':
        form= DonationForm(request.POST) 
        if form.is_valid():
            donation=form.save()

            # ************
            # donation.pay_status = 'True'
            # donation.save()  
            if donation.Certificate_80G:
                donation_id = donation.id
                donation_instance = Donation.objects.get(id=donation_id)
                year = str(datetime.now().year)
                id_keyword = f"NGO-80G-{year}-{donation_id}"
                pdf = sendMail(donation.name,id_keyword,donation.amount,donation.id,donation.email,donation.phone_number,donation.pan_card)
                g = Certificate_80g.objects.create(donater=donation_instance, Certificate_80G_no=id_keyword, pdf_file=pdf)
                g.save()
            # ********************  


            # param_dict={
            #     'MID': settings.PAYTM_MERCHANT_ID,
            #     'ORDER_ID': str(donation.id),
            #     'TXN_AMOUNT': str(donation.amount),
            #     'CUST_ID': donation.email,
            #     'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
            #     'WEBSITE':  settings.PAYTM_WEBSITE,
            #     'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
            #     'CALLBACK_URL':'http://127.0.0.1:8000/callback/',
            #     }
            

            # checksum = generate_checksum(param_dict , settings.PAYTM_SECRET_KEY)
            # donation.checksum = checksum
            # param_dict['CHECKSUMHASH'] = checksum
            # return render(request, 'account/redirect.html', context=param_dict)
            return render(request, "account/payment.html") 
        else:
            form = DonationForm()
    else:
        form = DonationForm()
    return render(request, "account/donation-details.html",{'form':form}) 

@csrf_exempt
def callback(request):
    # if request.method == 'POST':
    #     received_data = dict(request.POST)
    #     paytm_params = {}
    #     paytm_checksum = received_data['CHECKSUMHASH'][0]
    #     for key, value in received_data.items():
    #         if key == 'CHECKSUMHASH':
    #             paytm_checksum = value[0]
    #         else:
    #             paytm_params[key] = str(value[0])
    #     # Verify checksum
    #     is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
    #     if is_valid_checksum:
    #         received_data['message'] = "Checksum Matched"
    #     else:
    #         received_data['message'] = "Checksum Mismatched"
    #         return render(request, 'account/callback.html', context=received_data)
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = verify_checksum(response_dict, settings.PAYTM_SECRET_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Donation successful')
            
        else:
            print('Donation was not successful because' + response_dict['RESPMSG'])
    return render(request, 'account/callback.html', context=response_dict)

def blog_details(request):
    return render(request, "account/blog-details.html")     

def gallery(request):
    return render(request, "account/gallery.html") 

def gallery_ajax(request):
    data = Gallery.objects.all().order_by('-created_date')
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
