from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import signup_page,login_page,logout_page

urlpatterns = [
    path('login',login_page,name='login'),
    path('signup',signup_page,name='register'),
    path('logout',logout_page,name='logout'),     
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
