from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()

urlpatterns = [
    url(r'note/', views.noteclass.as_view(), name=None),
    url(r'retrieve/', views.notepost.as_view(), name=None)
]