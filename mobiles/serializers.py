
from rest_framework import serializers

from .models import Mobile
class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mobile
       
        fields='__all__'