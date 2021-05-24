from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

routers = routers.DefaultRouter()

urlpatterns = [
    url(r'home', views.index, name=None),
    url(r'create_note', views.make_note, name=None),
    url(r'display_note', views.list_note, name="display"),
    url(r'contact', views.contact, name=None)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
