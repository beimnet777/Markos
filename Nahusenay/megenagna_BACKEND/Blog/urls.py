from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import BlogView

router = DefaultRouter()
router.register('blog',BlogView,basename = 'blog')


urlpatterns = [
    path('',include(router.urls))
]
