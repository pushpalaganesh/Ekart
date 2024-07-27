from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','pname','pcost','pdetails','cat','is_active']

admin.site.register(Product)