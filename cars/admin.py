from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src = "{object.car_photo.url}" width = "40px" style = "border_radius: 100px" />')

    thumbnail.short_description = 'car photo'

    list_display = ('id','thumbnail','car_title', 
                    'state', 'color', 'model', 
                    'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    search_fields = ("id", "car_title", "fuel_type", "body_style")
    list_filter = ("fuel_type", "model", "body_style")
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Car, CarAdmin)