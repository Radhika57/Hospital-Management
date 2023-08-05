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
    
class FindingCategoryCreateAPIView(generics.CreateAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    
class FindingCategoryListView(ListAPIView):
    queryset = FindingCategory.objects.all()
    serializer_class = FindingCategorySerializer
    
class FindingCreateAPIView(generics.CreateAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class FindingListView(ListAPIView):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
    
class IncomeHeadCreateAPIView(generics.CreateAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    
class IncomeHeadListView(ListAPIView):
    queryset = IncomeHead.objects.all()
    serializer_class = IncomeHeadSerializer
    
class ExpenseHeadCreateAPIView(generics.CreateAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    
class ExpenseHeadListView(ListAPIView):
    queryset = ExpenseHead.objects.all()
    serializer_class = ExpenseHeadSerializer
    
class LeaveTypeCreateAPIView(generics.CreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    
class LeaveTypeListView(ListAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    
class DepartmentCreateAPIView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DesignationCreateAPIView(generics.CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class DesignationListView(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class SpecialistCreateAPIView(generics.CreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    
class SpecialistListView(ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    
class ReferralCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    
class ReferralCategoryListView(ListAPIView):
    queryset = ReferralCategory.objects.all()
    serializer_class = ReferralCategorySerializer
    
class ReferralCommissionCreateAPIView(generics.CreateAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    
class ReferralCommissionListView(ListAPIView):
    queryset = ReferralCommission.objects.all()
    serializer_class = ReferralCommissionSerializer
    
class ShiftCreateAPIView(generics.CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
class ShiftListView(ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
class ItemCategoryCreateAPIView(generics.CreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    
class ItemCategoryListView(ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    
class ItemStoreCreateAPIView(generics.CreateAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    
class ItemStoreListView(ListAPIView):
    queryset = ItemStore.objects.all()
    serializer_class = ItemStoreSerializer
    
class ItemSupplierCreateAPIView(generics.CreateAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer
    
class ItemSupplierListView(ListAPIView):
    queryset = ItemSupplier.objects.all()
    serializer_class = ItemSupplierSerializer