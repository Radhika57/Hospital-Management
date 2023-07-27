from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

class SuperAdminRegisterAPIView(APIView):
    serializer_class = SuperAdminCreateSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdminRegisterView(APIView):
    serializer_class = AdminCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = AdminCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Admin registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DoctorRegisterView(APIView):
    serializer_class = DoctorCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = DoctorCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Doctor registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AccountantRegisterView(APIView):
    serializer_class = AccountantCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = AccountantCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Accountant registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReceptionistRegisterView(APIView):
    serializer_class = ReceptionistCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = ReceptionistCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Receptionist registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PharmacistRegisterView(APIView):
    serializer_class = PharmacistCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = PharmacistCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Pharmacist registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PathologistRegisterView(APIView):
    serializer_class = PathologistCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = PathologistCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Pathologist registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RadiologistRegisterView(APIView):
    serializer_class = RadiologistCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = RadiologistCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Radiologist registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientRegisterView(APIView):
    serializer_class = PatientCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = PatientCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "Patient registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegisterView(APIView):
    serializer_class = UserCreateSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response({"message": "User registration successful."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            serializer = TokenObtainPairSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user
            if user.user_type == 'superadmin':
                response.data['user_type'] = 'superadmin'
            elif user.user_type == 'admin':
                response.data['user_type'] = 'admin'
            elif user.user_type == 'doctor':
                response.data['user_type'] = 'doctor'
            elif user.user_type == 'accountant':
                response.data['user_type'] = 'accountant'
            elif user.user_type == 'receptionist':
                response.data['user_type'] = 'receptionist'
            elif user.user_type == 'pharmacist':
                response.data['user_type'] = 'pharmacist'
            elif user.user_type == 'pathologist':
                response.data['user_type'] = 'pathologist'
            elif user.user_type == 'radiologist':
                response.data['user_type'] = 'radiologist'
            elif user.user_type == 'patient':
                response.data['user_type'] = 'patient'
            elif user.user_type == 'user':
                response.data['user_type'] = 'user'
            else:
                return Response({"message": "User doesn't exist."}, status=status.HTTP_201_CREATED)
                pass
        return response


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        # Invalidate the user's token
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    
class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='doctor')

class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class OutPatientCreateView(generics.CreateAPIView):
    queryset = OutPatient.objects.all()
    serializer_class = OutPatientSerializer

class InPatientCreateView(generics.CreateAPIView):
    queryset = InPatient.objects.all()
    serializer_class = InPatientSerializer
    
class MedicineCreateView(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
class PathologyTestCreateView(generics.CreateAPIView):
    queryset = PathologyTest.objects.all()
    serializer_class = PathologyTestSerializer
    
class BloodDonorCreateView(generics.CreateAPIView):
    queryset = BloodDonor.objects.all()
    serializer_class = BloodDonorSerializer
    
class PlateletsCreateAPIView(generics.CreateAPIView):
    queryset = Platelets.objects.all()
    serializer_class = PlateletsSerializer

class PlasmaCreateAPIView(generics.CreateAPIView):
    queryset = Plasma.objects.all()
    serializer_class = PlasmaSerializer

class CryodotCreateAPIView(generics.CreateAPIView):
    queryset = Cryodot.objects.all()
    serializer_class = CryodotSerializer

class WhiteCellsCreateAPIView(generics.CreateAPIView):
    queryset = WhiteCells.objects.all()
    serializer_class = WhiteCellsSerializer

class RedCellsCreateAPIView(generics.CreateAPIView):
    queryset = RedCells.objects.all()
    serializer_class = RedCellsSerializer

class CryoCreateAPIView(generics.CreateAPIView):
    queryset = Cryo.objects.all()
    serializer_class = CryoSerializer

class ComponentsCreateAPIView(generics.CreateAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentsSerializer
    
class AmbulanceCreateAPIView(generics.CreateAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    
class VisitorCreateAPIView(generics.CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    
class CallLogCreateAPIView(generics.CreateAPIView):
    queryset = CallLog.objects.all()
    serializer_class = CallLogSerializer
    
class ReceiveCreateAPIView(generics.CreateAPIView):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer
    
class DispatchCreateAPIView(generics.CreateAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    
class ComplainCreateAPIView(generics.CreateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    
class BirthRecordCreateAPIView(generics.CreateAPIView):
    queryset = BirthRecord.objects.all()
    serializer_class = BirthRecordSerializer
    
class DeathRecordCreateAPIView(generics.CreateAPIView):
    queryset = DeathRecord.objects.all()
    serializer_class = DeathRecordSerializer
    
class TPACreateAPIView(generics.CreateAPIView):
    queryset = TPA.objects.all()
    serializer_class = TPASerializer
    
class IncomeCreateAPIView(generics.CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer