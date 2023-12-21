from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from Room.views import allowed_users
from .models import Blog
from .serializer import BlogSerializer

# Create your views here.



# @method_decorator(allowed_users(),name='create')
# @method_decorator(allowed_users(),name='update')
# @method_decorator(allowed_users(),name='partial_update')
# @method_decorator(allowed_users(),name='destroy')
class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        # Specify the field to sort by (replace 'field_name' with your actual field name)
        queryset = queryset.order_by('-date')
        return queryset