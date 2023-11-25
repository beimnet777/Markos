from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import RoomProfile
from .serializer import RoomProfileSerializer
from django.utils.decorators import method_decorator
from .pagination import RoomProfilePagination

# Create your views here.

# Create your views here.
def allowed_users():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorize to view this page ")
        
        return wrapper_func
    return decorator



@method_decorator(allowed_users(),name='create')
@method_decorator(allowed_users(),name='update')
@method_decorator(allowed_users(),name='partial_update')
@method_decorator(allowed_users(),name='destroy')
class RoomProfileView(viewsets.ModelViewSet):
    queryset = RoomProfile.objects.all()
    serializer_class = RoomProfileSerializer 
    pagination_class = RoomProfilePagination
