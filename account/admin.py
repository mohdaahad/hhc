from django.contrib import admin
from .models import  Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display=('image', )
# Register your models here.
admin.site.register(Gallery,GalleryAdmin)