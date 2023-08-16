from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView , DestroyAPIView , RetrieveAPIView

class UnittypeCreateAPIView(generics.CreateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    
class UnittypeListView(ListAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    
class UnitTypeUpdateView(RetrieveUpdateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    lookup_field = 'pk' 
    
class UnitTypeDeleteView(DestroyAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    lookup_field = 'pk' 
    
class UnitTypeDetailView(RetrieveAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnittypeSerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class TaxCategoryCreateAPIView(generics.CreateAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    
class TaxCategoryListView(ListAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    
class TaxCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    lookup_field = 'pk' 
    
class TaxCategoryDeleteView(DestroyAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    lookup_field = 'pk' 
    
class TaxCategoryDetailView(RetrieveAPIView):
    queryset = TaxCategory.objects.all()
    serializer_class = TaxCategorySerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class ChargeTypeCreateAPIView(generics.CreateAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    
class ChargeTypeListView(ListAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    
class ChargeTypeUpdateView(RetrieveUpdateAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    lookup_field = 'pk' 
    
class ChargeTypeDeleteView(DestroyAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    lookup_field = 'pk' 
    
class ChargeTypeDetailView(RetrieveAPIView):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer
    lookup_field = 'pk'
    
####################################################################################################
    
class ChargeCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    
class ChargeCategoryListView(ListAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    
class ChargeCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    lookup_field = 'pk' 
    
class ChargeCategoryDeleteView(DestroyAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    lookup_field = 'pk' 
    
class ChargeCategoryDetailView(RetrieveAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class ChargesCreateAPIView(generics.CreateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    
class ChargesListView(ListAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    
class ChargesUpdateView(RetrieveUpdateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    lookup_field = 'pk' 
    
class ChargesDeleteView(DestroyAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    lookup_field = 'pk' 
    
class ChargesDetailView(RetrieveAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class FloorCreateAPIView(generics.CreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    
class FloorListView(ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    
class FloorUpdateView(RetrieveUpdateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'pk' 
    
class FloorDeleteView(DestroyAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'pk' 
    
class FloorDetailView(RetrieveAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'pk'
    
###################################################################################################
    
class BedTypeCreateAPIView(generics.CreateAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    
class BedTypeListView(ListAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    
class BedTypeUpdateView(RetrieveUpdateAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    lookup_field = 'pk' 
    
class BedTypeDeleteView(DestroyAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    lookup_field = 'pk' 
    
class BedTypeDetailView(RetrieveAPIView):
    queryset = BedType.objects.all()
    serializer_class = BedTypeSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class BedGroupCreateAPIView(generics.CreateAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    
class BedGroupListView(ListAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    
class BedGroupUpdateView(RetrieveUpdateAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    lookup_field = 'pk' 
    
class BedGroupDeleteView(DestroyAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    lookup_field = 'pk' 
    
class BedGroupDetailView(RetrieveAPIView):
    queryset = BedGroup.objects.all()
    serializer_class = BedGroupSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class BedCreateAPIView(generics.CreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    
class BedListView(ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    
class BedUpdateView(RetrieveUpdateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    lookup_field = 'pk' 
    
class BedDeleteView(DestroyAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    lookup_field = 'pk' 
    
class BedDetailView(RetrieveAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    lookup_field = 'pk'
    
#####################################################################################################

class PriorityCreateAPIView(generics.CreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class PriorityListView(ListAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    
class PriorityUpdateView(RetrieveUpdateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    lookup_field = 'pk' 
    
class PriorityDeleteView(DestroyAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    lookup_field = 'pk' 
    
class PriorityDetailView(RetrieveAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    lookup_field = 'pk'
    
###################################################################################################
    
class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    
class SourceListView(ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    
class SourceUpdateView(RetrieveUpdateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'pk' 
    
class SourceDeleteView(DestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'pk' 
    
class SourceDetailView(RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'pk'
    
##################################################################################################
    
class ComplainTypeCreateAPIView(generics.CreateAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    
class ComplainTypeListView(ListAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    
class ComplainTypeUpdateView(RetrieveUpdateAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    lookup_field = 'pk' 
    
class ComplainTypeDeleteView(DestroyAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    lookup_field = 'pk' 
    
class ComplainTypeDetailView(RetrieveAPIView):
    queryset = ComplainType.objects.all()
    serializer_class = ComplainTypeSerializer
    lookup_field = 'pk'
    
##################################################################################################
    
class PurposeCreateAPIView(generics.CreateAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer   

class PurposeListView(ListAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    
class PurposeUpdateView(RetrieveUpdateAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    lookup_field = 'pk' 
    
class PurposeDeleteView(DestroyAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    lookup_field = 'pk' 
    
class PurposeDetailView(RetrieveAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
    lookup_field = 'pk'
    
#################################################################################################
    
class OperationCategoryCreateAPIView(generics.CreateAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer   

class OperationCategoryListView(ListAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer
    
class OperationCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer
    lookup_field = 'pk' 
    
class OperationCategoryDeleteView(DestroyAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer
    lookup_field = 'pk' 
    
class OperationCategoryDetailView(RetrieveAPIView):
    queryset = OperationCategory.objects.all()
    serializer_class = OperationCategorySerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class OperationCreateAPIView(generics.CreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer   

class OperationListView(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    
class OperationUpdateView(RetrieveUpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    lookup_field = 'pk' 
    
class OperationDeleteView(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    lookup_field = 'pk' 
    
class OperationDetailView(RetrieveAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class MedicineCategoryCreateAPIView(generics.CreateAPIView):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer
    
class MedicineCategoryListView(ListAPIView):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer
    
class MedicineCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer
    lookup_field = 'pk' 
    
class MedicineCategoryDeleteView(DestroyAPIView):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer
    lookup_field = 'pk' 
    
class MedicineCategoryDetailView(RetrieveAPIView):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class MedicineSupplierCreateAPIView(generics.CreateAPIView):
    queryset = MedicineSupplier.objects.all()
    serializer_class = MedicineSupplierSerializer
    
class MedicineSupplierListView(ListAPIView):
    queryset = MedicineSupplier.objects.all()
    serializer_class = MedicineSupplierSerializer
    
class MedicineSupplierUpdateView(RetrieveUpdateAPIView):
    queryset = MedicineSupplier.objects.all()
    serializer_class = MedicineSupplierSerializer
    lookup_field = 'pk' 
    
class MedicineSupplierDeleteView(DestroyAPIView):
    queryset = MedicineSupplier.objects.all()
    serializer_class = MedicineSupplierSerializer
    lookup_field = 'pk' 
    
class MedicineSupplierDetailView(RetrieveAPIView):
    queryset = MedicineSupplier.objects.all()
    serializer_class = MedicineSupplierSerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class MedicineDosageCreateAPIView(generics.CreateAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    
class MedicineDosageListView(ListAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    
class MedicineDosageUpdateView(RetrieveUpdateAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    lookup_field = 'pk' 
    
class MedicineDosageDeleteView(DestroyAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    lookup_field = 'pk' 
    
class MedicineDosageDetailView(RetrieveAPIView):
    queryset = MedicineDosage.objects.all()
    serializer_class = MedicineDosageSerializer
    lookup_field = 'pk'
    
####################################################################################################
    
class DosageIntervalCreateAPIView(generics.CreateAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    
class DosageIntervalListView(ListAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    
class DosageIntervalUpdateView(RetrieveUpdateAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    lookup_field = 'pk' 
    
class DosageIntervalDeleteView(DestroyAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    lookup_field = 'pk' 
    
class DosageIntervalDetailView(RetrieveAPIView):
    queryset = DosageInterval.objects.all()
    serializer_class = DosageIntervalSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class DosageDurationCreateAPIView(generics.CreateAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    
class DosageDurationListView(ListAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    
class DosageDurationUpdateView(RetrieveUpdateAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    lookup_field = 'pk' 
    
class DosageDurationDeleteView(DestroyAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    lookup_field = 'pk' 
    
class DosageDurationDetailView(RetrieveAPIView):
    queryset = DosageDuration.objects.all()
    serializer_class = DosageDurationSerializer
    lookup_field = 'pk'
    
#####################################################################################################
    
class PathologyCategoryCreateAPIView(generics.CreateAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    
class PathologyCategoryListView(ListAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    
class PathologyCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    lookup_field = 'pk' 
    
class PathologyCategoryDeleteView(DestroyAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    lookup_field = 'pk' 
    
class PathologyCategoryDetailView(RetrieveAPIView):
    queryset = PathologyCategory.objects.all()
    serializer_class = PathologyCategorySerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class PathologyUnitCreateAPIView(generics.CreateAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    
class PathologyUnitListView(ListAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    
class PathologyUnitUpdateView(RetrieveUpdateAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    lookup_field = 'pk' 
    
class PathologyUnitDeleteView(DestroyAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    lookup_field = 'pk' 
    
class PathologyUnitDetailView(RetrieveAPIView):
    queryset = PathologyUnit.objects.all()
    serializer_class = PathologyUnitSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class PathologyParameterCreateAPIView(generics.CreateAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    
class PathologyParameterListView(ListAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    
class PathologyParameterUpdateView(RetrieveUpdateAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    lookup_field = 'pk' 
    
class PathologyParameterDeleteView(DestroyAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    lookup_field = 'pk' 
    
class PathologyParameterDetailView(RetrieveAPIView):
    queryset = PathologyParameter.objects.all()
    serializer_class = PathologyParameterSerializer
    lookup_field = 'pk'
    
######################################################################################################
    
class RadiologyCategoryCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    
class RadiologyCategoryListView(ListAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    
class RadiologyCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    lookup_field = 'pk' 
    
class RadiologyCategoryDeleteView(DestroyAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    lookup_field = 'pk' 
    
class RadiologyCategoryDetailView(RetrieveAPIView):
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
    lookup_field = 'pk'
    
##########################################################################################################
    
class RadiologyUnitCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    
class RadiologyUnitListView(ListAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    
class RadiologyUnitUpdateView(RetrieveUpdateAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    lookup_field = 'pk' 
    
class RadiologyUnitDeleteView(DestroyAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    lookup_field = 'pk' 
    
class RadiologyUnitDetailView(RetrieveAPIView):
    queryset = RadiologyUnit.objects.all()
    serializer_class = RadiologyUnitSerializer
    lookup_field = 'pk'
    
##########################################################################################################
    
class RadiologyParameterCreateAPIView(generics.CreateAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    
class RadiologyParameterListView(ListAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    
class RadiologyParameterUpdateView(RetrieveUpdateAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    lookup_field = 'pk' 
    
class RadiologyParameterDeleteView(DestroyAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    lookup_field = 'pk' 
    
class RadiologyParameterDetailView(RetrieveAPIView):
    queryset = RadiologyParameter.objects.all()
    serializer_class = RadiologyParameterSerializer
    lookup_field = 'pk'
    
##########################################################################################################

class BloodBankTypeCreateAPIView(generics.CreateAPIView):
    queryset = BloodBank_Type.objects.all()
    serializer_class = BloodBankTypeSerializer
    
class BloodBankTypeListView(ListAPIView):
    queryset = BloodBank_Type.objects.all()
    serializer_class = BloodBankTypeSerializer
    
class BloodBankTypeUpdateView(RetrieveUpdateAPIView):
    queryset = BloodBank_Type.objects.all()
    serializer_class = BloodBankTypeSerializer
    lookup_field = 'pk' 
    
class BloodBankTypeDeleteView(DestroyAPIView):
    queryset = BloodBank_Type.objects.all()
    serializer_class = BloodBankTypeSerializer
    lookup_field = 'pk' 
    
class BloodBankTypeDetailView(RetrieveAPIView):
    queryset = BloodBank_Type.objects.all()
    serializer_class = BloodBankTypeSerializer
    lookup_field = 'pk'
    
########################################################################################################
    
class BloodBankProductCreateAPIView(generics.CreateAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    
class BloodBankProductListView(ListAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    
class BloodBankProductUpdateView(RetrieveUpdateAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    lookup_field = 'pk' 
    
class BloodBankProductDeleteView(DestroyAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    lookup_field = 'pk' 
    
class BloodBankProductDetailView(RetrieveAPIView):
    queryset = BloodBank_Products.objects.all()
    serializer_class = BloodBankProductSerializer
    lookup_field = 'pk'
    
########################################################################################################
    
class SymptomsTypeCreateAPIView(generics.CreateAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    
class SymptomsTypeListView(ListAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    
class SymptomsTypeUpdateView(RetrieveUpdateAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    lookup_field = 'pk' 
    
class SymptomsTypeDeleteView(DestroyAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    lookup_field = 'pk' 
    
class SymptomsTypeDetailView(RetrieveAPIView):
    queryset = SymptomsType.objects.all()
    serializer_class = SymptomsTypeSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class SymptomsHeadCreateAPIView(generics.CreateAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    
class SymptomsHeadListView(ListAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    
class SymptomsHeadUpdateView(RetrieveUpdateAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    lookup_field = 'pk' 
    
class SymptomsHeadDeleteView(DestroyAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    lookup_field = 'pk' 
    
class SymptomsHeadDetailView(RetrieveAPIView):
    queryset = SymptomsHead.objects.all()
    serializer_class = SymptomsHeadSerializer
    lookup_field = 'pk'
    
########################################################################################################
    
class FindingCategoryCreateAPIView(generics.CreateAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    
class FindingCategoryListView(ListAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    
class FindingCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    lookup_field = 'pk' 
    
class FindingCategoryDeleteView(DestroyAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    lookup_field = 'pk' 
    
class FindingCategoryDetailView(RetrieveAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class FindingCreateAPIView(generics.CreateAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class FindingListView(ListAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class FindingUpdateView(RetrieveUpdateAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    lookup_field = 'pk' 
    
class FindingDeleteView(DestroyAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    lookup_field = 'pk' 
    
class FindingDetailView(RetrieveAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    lookup_field = 'pk'
    
#######################################################################################################    
    
class IncomeHeadCreateAPIView(generics.CreateAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    
class IncomeHeadListView(ListAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    
class IncomeHeadUpdateView(RetrieveUpdateAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    lookup_field = 'pk' 
    
class IncomeHeadDeleteView(DestroyAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    lookup_field = 'pk' 
    
class IncomeHeadDetailView(RetrieveAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    lookup_field = 'pk'
    
#######################################################################################################    
    
class ExpenseHeadCreateAPIView(generics.CreateAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    
class ExpenseHeadListView(ListAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    
class ExpenseHeadUpdateView(RetrieveUpdateAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    lookup_field = 'pk' 
    
class ExpenseHeadDeleteView(DestroyAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    lookup_field = 'pk' 
    
class ExpenseHeadDetailView(RetrieveAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    lookup_field = 'pk'
    
#######################################################################################################    
    
class LeaveTypeCreateAPIView(generics.CreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    
class LeaveTypeListView(ListAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    
class LeaveTypeUpdateView(RetrieveUpdateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    lookup_field = 'pk' 
    
class LeaveTypeDeleteView(DestroyAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    lookup_field = 'pk' 
    
class LeaveTypeDetailView(RetrieveAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class DepartmentCreateAPIView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentUpdateView(RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk' 
    
class DepartmentDeleteView(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk' 
    
class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class DesignationCreateAPIView(generics.CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class DesignationListView(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class DesignationUpdateView(RetrieveUpdateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk' 
    
class DesignationDeleteView(DestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk' 
    
class DesignationDetailView(RetrieveAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class SpecialistCreateAPIView(generics.CreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    
class SpecialistListView(ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    
class SpecialistUpdateView(RetrieveUpdateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    lookup_field = 'pk' 
    
class SpecialistDeleteView(DestroyAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    lookup_field = 'pk' 
    
class SpecialistDetailView(RetrieveAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ReferralCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    
class ReferralCategoryListView(ListAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    
class ReferralCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    lookup_field = 'pk' 
    
class ReferralCategoryDeleteView(DestroyAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    lookup_field = 'pk' 
    
class ReferralCategoryDetailView(RetrieveAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ReferralCommissionCreateAPIView(generics.CreateAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    
class ReferralCommissionListView(ListAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    
class ReferralCommissionUpdateView(RetrieveUpdateAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    lookup_field = 'pk' 
    
class ReferralCommissionDeleteView(DestroyAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    lookup_field = 'pk' 
    
class ReferralCommissionDetailView(RetrieveAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ShiftCreateAPIView(generics.CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
class ShiftListView(ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
class ShiftUpdateView(RetrieveUpdateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = 'pk' 
    
class ShiftDeleteView(DestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = 'pk' 
    
class ShiftDetailView(RetrieveAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ItemCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    
class ItemCategoryListView(ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    
class ItemCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    lookup_field = 'pk' 
    
class ItemCategoryDeleteView(DestroyAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    lookup_field = 'pk' 
    
class ItemCategoryDetailView(RetrieveAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ItemStoreCreateAPIView(generics.CreateAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    
class ItemStoreListView(ListAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    
class ItemStoreUpdateView(RetrieveUpdateAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    lookup_field = 'pk' 
    
class ItemStoreDeleteView(DestroyAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    lookup_field = 'pk' 
    
class ItemStoreDetailView(RetrieveAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    lookup_field = 'pk'
    
#######################################################################################################
    
class ItemSupplierCreateAPIView(generics.CreateAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    
class ItemSupplierListView(ListAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    
class ItemSupplierUpdateView(RetrieveUpdateAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    lookup_field = 'pk' 
    
class ItemSupplierDeleteView(DestroyAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    lookup_field = 'pk' 
    
class ItemSupplierDetailView(RetrieveAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    lookup_field = 'pk'
    
#######################################################################################################