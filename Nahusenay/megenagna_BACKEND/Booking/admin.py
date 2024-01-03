from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import Group, User
from Room.models import Room
from django.db.models import Q
class ModelAdmin(admin.ModelAdmin):
    ordering = ['payment_status', 'customer_first_name']
    list_filter = ['payment_status',"start_date", 'end_date']
    search_fields = ['customer_first_name', 'customer_last_name', 'customer_email']
    def save_model(self, request, obj, form, change):
        start_date = obj.start_date
        end_date  = obj.end_date
        overlapping_bookings = Booking.objects.filter((Q(start_date__lte=end_date) & Q(end_date__gte=start_date)),payment_status='approved' ).values('room')
        available_rooms = Room.objects.exclude(id__in=overlapping_bookings)
        
        if obj.room not in available_rooms:
            # Display an error message in the admin site
            self.message_user(request, "The Room you are trying to book  has already been booked in the time frame provided", level='ERROR')
        else:
            obj.save()
    
    # def get_queryset(self, request):
    #     start_date = request.GET.get('start_date')
    #     end_date = request.GET.get('end_date')

    #     if start_date and end_date:
    #         overlapping_bookings = Booking.objects.filter(
    #             (Q(start_date__lte=end_date) & Q(end_date__gte=start_date)),
    #             payment_status='approved'
    #         ).values('room')

    #         queryset = Room.objects.exclude(id__in=overlapping_bookings)
    #     else:
    #         queryset = Room.objects.all()

    #     return queryset

    
# Register your models here.
admin.site.register(Booking, ModelAdmin)
admin.site.unregister(Group)
admin.site.unregister(User) 
admin.site.site_header = 'Nahusenay Hotel Adminstration'    
