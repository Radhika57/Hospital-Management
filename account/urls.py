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
    path('api/create-outpatient/', OutPatientCreateView.as_view(), name='create_outpatient'),
    path('api/create-inpatient/', InPatientCreateView.as_view(), name='create_inpatient'),
    path('api/create-pathology-test/', PathologyTestCreateView.as_view(), name='create_pathology_test'),
    path('api/create-visitor/', VisitorCreateAPIView.as_view(), name='create_visitor'),
    
    path('api/create-patient/', PatientCreateView.as_view(), name='create_patient'),
    path('api/patients/', PatientListView.as_view(), name='patient-list'),
    
    path('api/create-dispatch/', DispatchCreateAPIView.as_view(), name='create_dispatch'),
    path('api/dispatch/', DispatchListView.as_view(), name='dispatch-list'),
    
    path('api/create-receive/', ReceiveCreateAPIView.as_view(), name='create_receive'),
    path('api/receive/', ReceiveListView.as_view(), name='receive-list'),
    
    path('purchase-medicine/', PurchaseMedicineListView.as_view(), name='purchase-medicine-list'),
    
    path('api/create-complain/', ComplainCreateAPIView.as_view(), name='create_complain'),
    path('api/complain/', ComplainListView.as_view(), name='complain-list'),
    
    path('api/create-calllog/', CallLogCreateAPIView.as_view(), name='create_calllog'),
    path('api/calllog/', CallLogListView.as_view(), name='calllog-list'),
    
    path('api/create-medicine/', MedicineCreateView.as_view(), name='create_medicine'),
    path('api/medicine/', MedicineListView.as_view(), name='medicine-list'),
    
    path('api/create-components/', ComponentsCreateAPIView.as_view(), name='create_components'),
    path('api/components/', ComponentsListView.as_view(), name='components-list'),
    
    path('api/create-bloodDonor/', BloodDonorCreateView.as_view(), name='create_bloodDonor'),
    path('api/bloodDonor/', BloodDonorListView.as_view(), name='bloodDonor-list'),
    
    path('api/create-ambulance/', AmbulanceCreateAPIView.as_view(), name='create_ambulance'),
    path('api/ambulance/', AmbulanceListView.as_view(), name='ambulance-list'),
    
    path('api/create-deathrecord/', DeathRecordCreateAPIView.as_view(), name='create_deathrecord'),
    path('api/deathrecord/', DeathRecordListView.as_view(), name='deathrecord-list'),
    
    path('api/create-birthrecord/', BirthRecordCreateAPIView.as_view(), name='create_birthrecord'),
    path('api/birthrecord/', BirthRecordListView.as_view(), name='birthrecord-list'),
    
    path('api/create-income/', IncomeCreateAPIView.as_view(), name='create_income'),
    path('api/income/', IncomeListView.as_view(), name='income-list'),
    
    path('api/create-expense/', ExpenseCreateAPIView.as_view(), name='create_expense'),
    path('api/expense/', ExpenseListView.as_view(), name='expense-list'),
    
    path('api/create-tpa/', TPACreateAPIView.as_view(), name='create_tpa'),
    path('api/tpa/', TPAListView.as_view(), name='tpa-list'),
    
    path('api/create-referralperson/', ReferralPersonCreateAPIView.as_view(), name='create_referralperson'),
    path('api/referralperson/', ReferralPersonListView.as_view(), name='referralperson-list'),
    
    path('api/create-item/', ItemCreateAPIView.as_view(), name='create_item'),
    path('api/item/', ItemListView.as_view(), name='item-list'),
    
    path('api/create-itemstock/', ItemStockCreateAPIView.as_view(), name='create_itemstock'),
    path('api/itemstock/', ItemStockListView.as_view(), name='itemstock-list'),
    
    
    
]
