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
    
class FloorCreateAPIView(generics.CreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    
class BedTypeCreateAPIView(generics.CreateAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    
class BedGroupCreateAPIView(generics.CreateAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    
class BedCreateAPIView(generics.CreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class PriorityCreateAPIView(generics.CreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    
class ComplainTypeCreateAPIView(generics.CreateAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    
class PurposeCreateAPIView(generics.CreateAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer   
