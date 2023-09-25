from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mens,womens,kids,accessories,single_product


urlpatterns = [
    path('mens',mens,name = 'mens'),
    path('womens',womens,name = 'womens'),
    path('kids',kids,name = 'kids'),
    path('accessories',accessories,name = 'accessories'),
    # path('single-product',single_product,name='single_product'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

