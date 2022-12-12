from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ThingSerializer
# Create your views here.
from .models import Mobile


class MobileListView(ListCreateAPIView):
    queryset=Mobile.objects.all()
    serializer_class= ThingSerializer


class MobileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Mobile.objects.all()
    serializer_class= ThingSerializer
