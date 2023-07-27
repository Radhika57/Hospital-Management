from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class UnittypeCreateAPIView(generics.CreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    
class TaxCategoryCreateAPIView(generics.CreateAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    
class ChargeTypeCreateAPIView(generics.CreateAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    
class ChargeCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    
class ChargesCreateAPIView(generics.CreateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    
