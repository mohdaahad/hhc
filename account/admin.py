from django.contrib import admin
from .models import  *
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms



class GalleryAdmin(admin.ModelAdmin):
    list_display=('image', )

class VolunteersForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(),
        }

class VolunteersAdmin(admin.ModelAdmin):
    form = VolunteersForm
    
class Social_VoluteersAdmin(admin.ModelAdmin):
    list_display=('volunteers','account' )

    
# Register your models here.

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Volunteers,VolunteersAdmin)
admin.site.register(Social_Voluteers,Social_VoluteersAdmin)