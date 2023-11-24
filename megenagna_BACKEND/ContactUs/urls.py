from django.urls import path
from .views import collect_feedback, get_feedbacks

urlpatterns = [
    path('postfeedback/', collect_feedback),
    path('getfeedback/', get_feedbacks)
]

