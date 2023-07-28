from django.urls import path
from .views import *
from rest_framework_simplejwt.views import( TokenObtainPairView,TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/login/', csrf_exempt(CustomTokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/superadmin/register', SuperAdminRegisterAPIView.as_view(), name='register'),
    path('api/admin/register', AdminRegisterView.as_view(), name='adminregister'),
    path('api/doctor/register', DoctorRegisterView.as_view(), name='doctorregister'),
    path('api/accountant/register', AccountantRegisterView.as_view(), name='accountantregister'),
    path('api/receptionist/register', ReceptionistRegisterView.as_view(), name='receptionistregister'),
    path('api/pharmacist/register', PharmacistRegisterView.as_view(), name='pharmacistregister'),
    path('api/pathologist/register', PathologistRegisterView.as_view(), name='pathologistregister'),
    path('api/radiologist/register', RadiologistRegisterView.as_view(), name='radiologistregister'),
    path('api/patient/register', PatientRegisterView.as_view(), name='patientregister'),
    path('api/user/register', UserRegisterView.as_view(), name='userregister'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/create-appointment/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('api/create-patient/', PatientCreateView.as_view(), name='create_patient'),
    path('api/patients/', PatientListView.as_view(), name='patient-list'),
    
    path('api/create-outpatient/', OutPatientCreateView.as_view(), name='create_outpatient'),
    path('api/create-inpatient/', InPatientCreateView.as_view(), name='create_inpatient'),
    path('api/create-medicine/', MedicineCreateView.as_view(), name='create_medicine'),
    path('api/create-pathology-test/', PathologyTestCreateView.as_view(), name='create_pathology_test'),
    path('api/create-bloodDonor/', BloodDonorCreateView.as_view(), name='create_bloodDonor'),
    path('api/create-components/', ComponentsCreateAPIView.as_view(), name='create_components'),
    path('api/create-ambulance/', AmbulanceCreateAPIView.as_view(), name='create_ambulance'),
    path('api/create-visitor/', VisitorCreateAPIView.as_view(), name='create_visitor'),
    path('api/create-calllog/', CallLogCreateAPIView.as_view(), name='create_calllog'),
    path('api/create-receive/', ReceiveCreateAPIView.as_view(), name='create_receive'),
    path('api/create-dispatch/', DispatchCreateAPIView.as_view(), name='create_dispatch'),
    path('api/create-complain/', ComplainCreateAPIView.as_view(), name='create_complain'),
    path('api/create-birthrecord/', BirthRecordCreateAPIView.as_view(), name='create_birthrecord'),
    path('api/create-deathrecord/', DeathRecordCreateAPIView.as_view(), name='create_deathrecord'),
    path('api/create-tpa/', TPACreateAPIView.as_view(), name='create_tpa'),
    path('api/create-income/', IncomeCreateAPIView.as_view(), name='create_income'),
]
