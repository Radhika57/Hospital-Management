from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

class UnittypeCreateAPIView(generics.CreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    
class UnittypeListView(ListAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    
class TaxCategoryCreateAPIView(generics.CreateAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    
class TaxCategoryListView(ListAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    
class ChargeTypeCreateAPIView(generics.CreateAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    
class ChargeTypeListView(ListAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    
class ChargeCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    
class ChargeCategoryListView(ListAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    
class ChargesCreateAPIView(generics.CreateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    
class ChargesListView(ListAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    
class FloorCreateAPIView(generics.CreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    
class FloorListView(ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    
class BedTypeCreateAPIView(generics.CreateAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    
class BedTypeListView(ListAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    
class BedGroupCreateAPIView(generics.CreateAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    
class BedGroupListView(ListAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    
class BedCreateAPIView(generics.CreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    
class BedListView(ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class PriorityCreateAPIView(generics.CreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class PriorityListView(ListAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    
class SourceListView(ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    
class ComplainTypeCreateAPIView(generics.CreateAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    
class ComplainTypeListView(ListAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    
class PurposeCreateAPIView(generics.CreateAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer   

class PurposeListView(ListAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    
class OperationCategoryCreateAPIView(generics.CreateAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer   

class OperationCategoryListView(ListAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer
    
class OperationCreateAPIView(generics.CreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer   

class OperationListView(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    
class MedicineDosageCreateAPIView(generics.CreateAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    
class MedicineDosageListView(ListAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    
class DosageIntervalCreateAPIView(generics.CreateAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    
class DosageIntervalListView(ListAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    
class DosageDurationCreateAPIView(generics.CreateAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    
class DosageDurationListView(ListAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    
class PathologyCategoryCreateAPIView(generics.CreateAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    
class PathologyCategoryListView(ListAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    
class PathologyUnitCreateAPIView(generics.CreateAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    
class PathologyUnitListView(ListAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    
class PathologyParameterCreateAPIView(generics.CreateAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    
class PathologyParameterListView(ListAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    
class RadiologyCategoryCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    
class RadiologyCategoryListView(ListAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    
class RadiologyUnitCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    
class RadiologyUnitListView(ListAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    
class RadiologyParameterCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    
class RadiologyParameterListView(ListAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    
class BloodBankProductCreateAPIView(generics.CreateAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    
class BloodBankProductListView(ListAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    
class SymptomsTypeCreateAPIView(generics.CreateAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    
class SymptomsTypeListView(ListAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    
class SymptomsHeadCreateAPIView(generics.CreateAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    
class SymptomsHeadListView(ListAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer