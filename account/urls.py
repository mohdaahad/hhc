from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('donation-listing/', views.donation_listing, name='donation_listing'),
    path('blog/', views.blog, name='blog'),
    path('events/', views.events, name='events'),
    path('faq/', views.faq, name='faq'),
    path('service/', views.service, name='service'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('donation-details/', views.donation_details, name='donation_details'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('join_volunteers/', views.join_volunteers, name='join_volunteers'),
    path('ajax_gallery/', views.gallery_ajax, name='ajax_gallery'),
    path('volunteers_ajax/', views.volunteers_ajax, name='volunteers_ajax'),

]