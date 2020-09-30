# from django.shortcuts import render
from .models import counting
from rest_framework import viewsets
from .Serializers import countSerializer
# # Create your views here.
class countingViewSet(viewsets.ModelViewSet):
    queryset = counting.objects.all()
    serializer_class = countSerializer