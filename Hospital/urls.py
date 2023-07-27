"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import( TokenObtainPairView,TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView
from account.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('settings/', include('settings.urls')),
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
