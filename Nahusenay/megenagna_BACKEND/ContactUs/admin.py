from django.contrib import admin
from .models import ContactUS

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    ordering = ['date']

admin.site.register( ContactUS, ModelAdmin )