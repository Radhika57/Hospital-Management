from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields =  ('staff_id','role','designation','department','specialist',
                   'first_name','last_name','father_name','mother_name','gender',
                   'marital_status','blood_group','dob','date_of_joining','phone',
                   'emergency_contact','email','photo','current_address','permanent_address'
                   ,'qualification','work_experience','specialization','note','pan_number',
                   'national_identification_number','local_identification_number','reference_contact',
                   'epf_number','basic_salary','contract_type','work_shift','work_location','casual_leave',
                   'privilege_leave','sick_leave','maternity_leave','paternity_leave','fever_leave','account_title',
                   'bank_account_no','bank_name','ifsc_code','bank_branch_name','facebook_url','twitter_url',
                   'linkedin_url','instagram_url','resume','joining_letter','other_document')

          
            
# class SuperAdminCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'superadmin'
#         return super().create(validated_data)
    
# class AdminCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'admin'
#         return super().create(validated_data)
    
# class DoctorCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'doctor'
#         return super().create(validated_data)
    
# class AccountantCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'accountant'
#         return super().create(validated_data)
    
# class ReceptionistCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'receptionist'
#         return super().create(validated_data)
    
# class PharmacistCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'pharmacist'
#         return super().create(validated_data)
    
# class PathologistCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'pathologist'
#         return super().create(validated_data)
    
# class RadiologistCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'radiologist'
#         return super().create(validated_data)
    
# class PatientCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'patient'
#         return super().create(validated_data)
    
# class UserCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         validated_data['user_type'] = 'user'
#         return super().create(validated_data)


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_user_type = serializers.SerializerMethodField(method_name='get_doctor_user_type')

    class Meta:
        model = Appointment
        fields = '__all__'
    
    def get_doctor_user_type(self, obj):
        try:
            doctor_user = obj.doctor
            return doctor_user.user_type if doctor_user else None
        except CustomUser.DoesNotExist:
            return None  
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
  
class OutPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPatient
        fields = '__all__'  
        
class InPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = InPatient
        fields = '__all__'   
        
class TestParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestParameter
        fields = '__all__'


class PathologyTestSerializer(serializers.ModelSerializer):
    parameters = TestParameterSerializer(many=True)

    class Meta:
        model = PathologyTest
        fields = '__all__'

    def create(self, validated_data):
        parameters_data = validated_data.pop('parameters', [])
        pathology_test = PathologyTest.objects.create(**validated_data)
        for param_data in parameters_data:
            TestParameter.objects.create(pathology_test=pathology_test, **param_data)
        return pathology_test

    def validate(self, data):
        test_parameter_name = data.get('test_parameter_name', None)
        if test_parameter_name and test_parameter_name != 'select':
            # Set reference_range and unit based on test_parameter_name
            if test_parameter_name == 'rbc':
                data['reference_range'] = '4.1 to 5.1 million/mm3'
                data['unit'] = 'million/mm3'
            elif test_parameter_name == 'liver function test':
                data['reference_range'] = '7 to 55 units per liter'
                data['unit'] = '(U/L)'
            elif test_parameter_name == 'tsh(thyroid stimulation hormone)':
                data['reference_range'] = '0.5 to 3.0'
                data['unit'] = '(U/L)'

        return data 
        
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'
        
class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'
        
class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = '__all__'
        
class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
        
class CallLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallLog
        fields = '__all__'
        
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'  
        
class PurchaseMedicineSerializer(serializers.ModelSerializer):
    medicine_name = MedicineSerializer(source='medicine', read_only=True)
    tax = serializers.FloatField(source='medicine.tax', read_only=True)

    class Meta:
        model = PurchaseMedicine
        fields = '__all__'
        
class PlateletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platelets
        fields = '__all__'

class PlasmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plasma
        fields = '__all__'

class CryodotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryodot
        fields = '__all__'

class WhiteCellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteCells
        fields = '__all__'

class RedCellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedCells
        fields = '__all__'

class CryoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryo
        fields = '__all__'

class ComponentsSerializer(serializers.ModelSerializer):
    platelets = PlateletsSerializer()
    plasma = PlasmaSerializer()
    cryodot = CryodotSerializer()
    whitecells = WhiteCellsSerializer()
    redcells = RedCellsSerializer()
    cryo = CryoSerializer()

    class Meta:
        model = Components
        fields = '__all__'

    def create(self, validated_data):
        platelets_data = validated_data.pop('platelets')
        plasma_data = validated_data.pop('plasma')
        cryodot_data = validated_data.pop('cryodot')
        whitecells_data = validated_data.pop('whitecells')
        redcells_data = validated_data.pop('redcells')
        cryo_data = validated_data.pop('cryo')

        platelets = Platelets.objects.create(**platelets_data)
        plasma = Plasma.objects.create(**plasma_data)
        cryodot = Cryodot.objects.create(**cryodot_data)
        whitecells = WhiteCells.objects.create(**whitecells_data)
        redcells = RedCells.objects.create(**redcells_data)
        cryo = Cryo.objects.create(**cryo_data)

        components = Components.objects.create(
            platelets=platelets,
            plasma=plasma,
            cryodot=cryodot,
            whitecells=whitecells,
            redcells=redcells,
            cryo=cryo,
            **validated_data
        )

        return components
        
class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = '__all__'
        
class BirthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthRecord
        fields = '__all__'
        
class DeathRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeathRecord
        fields = '__all__'
        
class TPASerializer(serializers.ModelSerializer):
    class Meta:
        model = TPA
        fields = '__all__'
        
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        
class ReferralPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralPerson
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class ItemStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStock
        fields = '__all__'
        
class BloodDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonor
        fields = '__all__'