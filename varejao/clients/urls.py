from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactList

urlpatterns = [
    path('', ContactList.as_view()),
]