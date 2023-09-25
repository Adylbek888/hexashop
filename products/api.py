from .models import *  
from rest_framework import viewsets,permissions
from .serializers import *


class MenApi(viewsets.ModelViewSet):
    queryset = Mens.objects.all()
    serializer_class = MenSerializer

class WomenApi(viewsets.ModelViewSet):
    queryset = Womens.objects.all()
    serializer_class = WomenSerializer    


class KidApi(viewsets.ModelViewSet):
    queryset = Kids.objects.all()
    serializer_class = KidSerializer    


class AccessoryApi(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessorySerializer  