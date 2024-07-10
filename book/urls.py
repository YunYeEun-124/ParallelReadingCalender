from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import*

router = DefaultRouter()

router.register(r'book',BookViewSet)

urlpatterns = [
   path('',include(router.urls)),
]