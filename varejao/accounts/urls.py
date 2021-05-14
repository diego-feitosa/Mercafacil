from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountList

urlpatterns = [
    path('', AccountList.as_view()),
]