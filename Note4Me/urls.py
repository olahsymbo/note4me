from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

admin.site.site_header = "Note4me"
admin.site.site_title = "Note4me"
admin.site.index_title = ""

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url('', include('NoteApp.urls')),
]
