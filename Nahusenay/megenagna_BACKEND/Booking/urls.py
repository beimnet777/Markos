from django.urls import path
from .views import book, check_availability, check_payment

urlpatterns = [
    path('book/', book),
    path('available/<str:start_date>/<str:end_date>/', check_availability),
    path('check_payment/<str:unique_id>', check_payment)
]