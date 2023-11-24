from django.urls import path, include

from .views import RoomProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('roomprofile',RoomProfileView,basename='roomprofile')

urlpatterns = [
    path('rooms/',include(router.urls)),
]
