from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

from rest_framework import routers
from products.api import *

router = routers.DefaultRouter()
router.register('api/mens',MenApi,'menApi')
router.register('api/womens',WomenApi,'womenApi')
router.register('api/kids',KidApi,'kidApi')
router.register('api/accessory',AccessoryApi,'accessoryApi')






urlpatterns = [
    path("admin/", admin.site.urls),
    path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('',include('main.urls')),
    path('',include(router.urls)),
    path('products/',include('products.urls')),
    path('auth/',include('auth_custom.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)