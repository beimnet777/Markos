from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import Group, User

class ModelAdmin(admin.ModelAdmin):
    ordering = ['created_at', 'start_date']
    # def get_queryset(self, request):
    #     # queryset = super().get_queryset(request)
    #     # filtered_queryset = queryset.filter(payment_status = 'Approved')
        
    #     return filtered_queryset
    
# Register your models here.
admin.site.register(Booking, ModelAdmin)
admin.site.unregister(Group)
admin.site.unregister(User) 
admin.site.site_header = 'Nahusenay Hotel Adminstration'    
