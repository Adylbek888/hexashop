from .models import *
from rest_framework import serializers

class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mens
        fields = '__all__'

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Womens
        fields = '__all__'

class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kids
        fields = '__all__'

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'                