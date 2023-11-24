from django.contrib import admin
from .models import Booking

class ModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        filtered_queryset = queryset.filter(payment_status = 'Approved')
        return filtered_queryset
    
# Register your models here.
admin.site.register(Booking)
