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