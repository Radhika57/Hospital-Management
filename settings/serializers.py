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