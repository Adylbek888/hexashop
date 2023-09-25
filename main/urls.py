from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import about,contacts,index
from django.views.generic import TemplateView

urlpatterns = [
   
    path('',index,name='home'), 
    path('about',about,name='about'),
    path('contacts',contacts,name='contacts'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
