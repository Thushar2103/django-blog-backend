from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blog', BlogpostViewSet)

urlpatterns = [
    path('', include(router.urls)),
     
] 