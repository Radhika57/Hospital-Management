from django.urls import path
from .views import *
from rest_framework_simplejwt.views import( TokenObtainPairView,TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/login/', csrf_exempt(CustomTokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register_staff/', StaffRegistration.as_view(), name='register_staff'),
    # path('api/superadmin/register', SuperAdminRegisterAPIView.as_view(), name='register'),
    # path('api/admin/register', AdminRegisterView.as_view(), name='adminregister'),
    # path('api/doctor/register', DoctorRegisterView.as_view(), name='doctorregister'),
    # path('api/accountant/register', AccountantRegisterView.as_view(), name='accountantregister'),
    # path('api/receptionist/register', ReceptionistRegisterView.as_view(), name='receptionistregister'),
    # path('api/pharmacist/register', PharmacistRegisterView.as_view(), name='pharmacistregister'),
    # path('api/pathologist/register', PathologistRegisterView.as_view(), name='pathologistregister'),
    # path('api/radiologist/register', RadiologistRegisterView.as_view(), name='radiologistregister'),
    # path('api/patient/register', PatientRegisterView.as_view(), name='patientregister'),
    # path('api/user/register', UserRegisterView.as_view(), name='userregister'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    
    
    path('api/create-appointment/', AppointmentCreateView.as_view(), name='create_appointment'),
    path('api/create-outpatient/', OutPatientCreateView.as_view(), name='create_outpatient'),
    path('api/create-inpatient/', InPatientCreateView.as_view(), name='create_inpatient'),
    path('api/create-pathology-test/', PathologyTestCreateView.as_view(), name='create_pathology_test'),
    path('api/create-visitor/', VisitorCreateAPIView.as_view(), name='create_visitor'),
    
    path('api/create-patient/', PatientCreateView.as_view(), name='create_patient'),
    path('api/patients/', PatientListView.as_view(), name='patient-list'),
    path('api/patient/<int:pk>/', PatientUpdateView.as_view(), name='patient-update'),
    path('api/patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    path('api/patient/<int:pk>/detail/', PatientDetailView.as_view(), name='patient-detail'),
    
    path('api/create-dispatch/', DispatchCreateAPIView.as_view(), name='create_dispatch'),
    path('api/dispatch/', DispatchListView.as_view(), name='dispatch-list'),
    path('api/dispatch/<int:pk>/', DispatchUpdateView.as_view(), name='dispatch-update'),
    path('api/dispatch/<int:pk>/delete/', DispatchDeleteView.as_view(), name='dispatch-delete'),
    path('api/dispatch/<int:pk>/detail/', DispatchDetailView.as_view(), name='dispatch-detail'),
    
    path('api/create-receive/', ReceiveCreateAPIView.as_view(), name='create_receive'),
    path('api/receive/', ReceiveListView.as_view(), name='receive-list'),
    path('api/receive/<int:pk>/', ReceiveUpdateView.as_view(), name='receive-update'),
    path('api/receive/<int:pk>/delete/', ReceiveDeleteView.as_view(), name='receive-delete'),
    path('api/receive/<int:pk>/detail/', ReceiveDetailView.as_view(), name='receive-detail'),
    
    path('api/create_purchase-medicine/', PurchaseMedicineCreateView.as_view(), name='create_purchase-medicine'),
    path('api/purchase-medicine/', PurchaseMedicineListView.as_view(), name='purchase-medicine-list'),
    path('api/purchase-medicine/<int:pk>/', PurchaseMedicineUpdateView.as_view(), name='purchase-medicine-update'),
    path('api/purchase-medicine/<int:pk>/delete/', PurchaseMedicineDeleteView.as_view(), name='purchase-medicine-delete'),
    path('api/purchase-medicine/<int:pk>/detail/', PurchaseMedicineDetailView.as_view(), name='purchase-medicine-detail'),
    
    path('api/create-complain/', ComplainCreateAPIView.as_view(), name='create_complain'),
    path('api/complain/', ComplainListView.as_view(), name='complain-list'),
    path('api/complain/<int:pk>/', ComplainUpdateView.as_view(), name='complain-update'),
    path('api/complain/<int:pk>/delete/', ComplainDeleteView.as_view(), name='complain-delete'),
    path('api/complain/<int:pk>/detail/', ComplainDetailView.as_view(), name='complain-detail'),
    
    path('api/create-calllog/', CallLogCreateAPIView.as_view(), name='create_calllog'),
    path('api/calllog/', CallLogListView.as_view(), name='calllog-list'),
    path('api/calllog/<int:pk>/', CallLogUpdateView.as_view(), name='calllog-update'),
    path('api/calllog/<int:pk>/delete/', CallLogDeleteView.as_view(), name='calllog-delete'),
    path('api/calllog/<int:pk>/detail/', CallLogDetailView.as_view(), name='calllog-detail'),
    
    path('api/create-medicine/', MedicineCreateView.as_view(), name='create_medicine'),
    path('api/medicine/', MedicineListView.as_view(), name='medicine-list'),
    path('api/medicine/<int:pk>/', MedicineUpdateView.as_view(), name='medicine-update'),
    path('api/medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine-delete'),
    path('api/medicine/<int:pk>/detail/', MedicineDetailView.as_view(), name='medicine-detail'),
    
    path('api/create-components/', ComponentsCreateAPIView.as_view(), name='create_components'),
    path('api/components/', ComponentsListView.as_view(), name='components-list'),
    path('api/components/<int:pk>/', ComponentsUpdateView.as_view(), name='components-update'),
    path('api/components/<int:pk>/delete/', ComponentsDeleteView.as_view(), name='components-delete'),
    path('api/components/<int:pk>/detail/', ComponentsDetailView.as_view(), name='components-detail'),
    
    path('api/create-bloodDonor/', BloodDonorCreateView.as_view(), name='create_bloodDonor'),
    path('api/bloodDonor/', BloodDonorListView.as_view(), name='bloodDonor-list'),
    path('api/bloodDonor/<int:pk>/', BloodDonorUpdateView.as_view(), name='bloodDonor-update'),
    path('api/bloodDonor/<int:pk>/delete/', BloodDonorDeleteView.as_view(), name='bloodDonor-delete'),
    path('api/bloodDonor/<int:pk>/detail/', BloodDonorDetailView.as_view(), name='bloodDonor-detail'),
    
    path('api/create-ambulance/', AmbulanceCreateAPIView.as_view(), name='create_ambulance'),
    path('api/ambulance/', AmbulanceListView.as_view(), name='ambulance-list'),
    path('api/ambulance/<int:pk>/', AmbulanceUpdateView.as_view(), name='ambulance-update'),
    path('api/ambulance/<int:pk>/delete/', AmbulanceDeleteView.as_view(), name='ambulance-delete'),
    path('api/ambulance/<int:pk>/detail/', AmbulanceDetailView.as_view(), name='ambulance-detail'),
    
    path('api/create-deathrecord/', DeathRecordCreateAPIView.as_view(), name='create_deathrecord'),
    path('api/deathrecord/', DeathRecordListView.as_view(), name='deathrecord-list'),
    path('api/deathrecord/<int:pk>/', DeathRecordUpdateView.as_view(), name='deathrecord-update'),
    path('api/deathrecord/<int:pk>/delete/', DeathRecordDeleteView.as_view(), name='deathrecord-delete'),
    path('api/deathrecord/<int:pk>/detail/', DeathRecordDetailView.as_view(), name='deathrecord-detail'),
    
    path('api/create-birthrecord/', BirthRecordCreateAPIView.as_view(), name='create_birthrecord'),
    path('api/birthrecord/', BirthRecordListView.as_view(), name='birthrecord-list'),
    path('api/birthrecord/<int:pk>/', BirthRecordUpdateView.as_view(), name='birthrecord-update'),
    path('api/birthrecord/<int:pk>/delete/', BirthRecordDeleteView.as_view(), name='birthrecord-delete'),
    path('api/birthrecord/<int:pk>/detail/', BirthRecordDetailView.as_view(), name='birthrecord-detail'),
    
    path('api/create-income/', IncomeCreateAPIView.as_view(), name='create_income'),
    path('api/income/', IncomeListView.as_view(), name='income-list'),
    path('api/income/<int:pk>/', IncomeUpdateView.as_view(), name='income-update'),
    path('api/income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
    path('api/income/<int:pk>/detail/', IncomeDetailView.as_view(), name='income-detail'),
    
    path('api/create-expense/', ExpenseCreateAPIView.as_view(), name='create_expense'),
    path('api/expense/', ExpenseListView.as_view(), name='expense-list'),
    path('api/expense/<int:pk>/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('api/expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('api/expense/<int:pk>/detail/', ExpenseDetailView.as_view(), name='expense-detail'),
    
    path('api/create-tpa/', TPACreateAPIView.as_view(), name='create_tpa'),
    path('api/tpa/', TPAListView.as_view(), name='tpa-list'),
    path('api/tpa/<int:pk>/', TPAUpdateView.as_view(), name='tpa-update'),
    path('api/tpa/<int:pk>/delete/', TPADeleteView.as_view(), name='tpa-delete'),
    path('api/tpa/<int:pk>/detail/', TPADetailView.as_view(), name='tpa-detail'),
    
    path('api/create-referralperson/', ReferralPersonCreateAPIView.as_view(), name='create_referralperson'),
    path('api/referralperson/', ReferralPersonListView.as_view(), name='referralperson-list'),
    path('api/referralperson/<int:pk>/', ReferralPersonUpdateView.as_view(), name='referralperson-update'),
    path('api/referralperson/<int:pk>/delete/', ReferralPersonDeleteView.as_view(), name='referralperson-delete'),
    path('api/referralperson/<int:pk>/detail/', ReferralPersonDetailView.as_view(), name='referralperson-detail'),
    
    path('api/create-item/', ItemCreateAPIView.as_view(), name='create_item'),
    path('api/item/', ItemListView.as_view(), name='item-list'),
    path('api/item/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('api/item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('api/item/<int:pk>/detail/', ItemDetailView.as_view(), name='item-detail'),
    
    path('api/create-itemstock/', ItemStockCreateAPIView.as_view(), name='create_itemstock'),
    path('api/itemstock/', ItemStockListView.as_view(), name='itemstock-list'),
    path('api/itemstock/<int:pk>/', ItemStockUpdateView.as_view(), name='itemstock-update'),
    path('api/itemstock/<int:pk>/delete/', ItemStockDeleteView.as_view(), name='itemstock-delete'),
    path('api/itemstock/<int:pk>/detail/', ItemStockDetailView.as_view(), name='itemstock-detail'),
    
    
    
]
