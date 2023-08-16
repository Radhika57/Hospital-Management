from rest_framework import serializers
from .models import *

class UnittypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'
        
class TaxCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCategory
        fields = '__all__'
        
class ChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeType
        fields = '__all__'
        
class ChargeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeCategory
        fields = '__all__'
        
class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charges
        fields = '__all__'
        
class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'
        
class BedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedType
        fields = '__all__'
        
class BedGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedGroup
        fields = '__all__'
        
class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'
        
class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'
        
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
        
class ComplainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainType
        fields = '__all__'
        
class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = '__all__'
        
class OperationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationCategory
        fields = '__all__'
        
class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
        
class MedicineDosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDosage
        fields = '__all__'
        
class MedicineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineCategory
        fields = '__all__'
        
class MedicineSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineSupplier
        fields = '__all__'
        
class DosageIntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageInterval
        fields = '__all__'
        
class DosageDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageDuration
        fields = '__all__'
        
class PathologyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologyCategory
        fields = '__all__'
        
class PathologyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologyUnit
        fields = '__all__'
        
class PathologyParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologyParameter
        fields = '__all__'
        
class RadiologyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyCategory
        fields = '__all__'
        
class RadiologyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyUnit
        fields = '__all__'
        
class RadiologyParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyParameter
        fields = '__all__'
        
class BloodBankTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank_Type
        fields = '__all__'
        
class BloodBankProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank_Products
        fields = '__all__'
        
class SymptomsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomsType
        fields = '__all__'
        
class SymptomsHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomsHead
        fields = '__all__'
        
class FindingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FindingCategory
        fields = '__all__'
        
class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = '__all__'
        
class IncomeHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeHead
        fields = '__all__'
        
class ExpenseHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseHead
        fields = '__all__'
        
class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
        
class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'
        
class ReferralCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCategory
        fields = '__all__'
        
class ReferralCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCommission
        fields = '__all__'
        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        
class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'
        
class ItemStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStore
        fields = '__all__'
        
class ItemSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSupplier
        fields = '__all__'
        