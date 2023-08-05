from django.urls import path, include
from settings.views import *

urlpatterns = [
    path('api/create-unittype/', UnittypeCreateAPIView.as_view(), name='create_unittype'),
    path('api/unittype/', UnittypeListView.as_view(), name='unittype-list'),
    
    path('api/create-taxcategory/', TaxCategoryCreateAPIView.as_view(), name='create_taxcategory'),
    path('api/taxcategory/', TaxCategoryListView.as_view(), name='taxcategory-list'),
    
    path('api/create-chargetype/', ChargeTypeCreateAPIView.as_view(), name='create_chargetype'),
    path('api/chargetype/', ChargeTypeListView.as_view(), name='chargetype-list'),
    
    path('api/create-chargecategory/', ChargeCategoryCreateAPIView.as_view(), name='create_chargecategory'),
    path('api/chargecategory/', ChargeCategoryListView.as_view(), name='chargecategory-list'),
    
    path('api/create-charges/', ChargesCreateAPIView.as_view(), name='create_charges'),
    path('api/charges/', ChargesListView.as_view(), name='charges-list'),
    
    path('api/create-floor/', FloorCreateAPIView.as_view(), name='create_floor'),
    path('api/floor/', FloorListView.as_view(), name='floor-list'),
    
    path('api/create-bedtype/', BedTypeCreateAPIView.as_view(), name='create_bedtype'),
    path('api/bedtype/', BedTypeListView.as_view(), name='bedtype-list'),
    
    path('api/create-bedgroup/', BedGroupCreateAPIView.as_view(), name='create_bedgroup'),
    path('api/bedgroup/', BedGroupListView.as_view(), name='bedgroup-list'),
    
    path('api/create-bed/', BedCreateAPIView.as_view(), name='create_bed'),
    path('api/bed/', BedListView.as_view(), name='bed-list'),
    
    path('api/create-priority/', PriorityCreateAPIView.as_view(), name='create_priority'),
    path('api/priority/', PriorityListView.as_view(), name='priority-list'),
    
    path('api/create-source/', SourceCreateAPIView.as_view(), name='create_source'),
    path('api/source/', SourceListView.as_view(), name='source-list'),
    
    path('api/create-complaintype/', ComplainTypeCreateAPIView.as_view(), name='create_complaintype'),
    path('api/complaintype/', ComplainTypeListView.as_view(), name='complaintype-list'),
    
    path('api/create-purpose/', PurposeCreateAPIView.as_view(), name='create_purpose'),
    path('api/purpose/', PurposeListView.as_view(), name='purpose-list'),
    
    path('api/create-operationcategory/', OperationCategoryCreateAPIView.as_view(), name='create_operationcategory'),
    path('api/operationcategory/', OperationCategoryListView.as_view(), name='operationcategory-list'),
    
    path('api/create-operation/', OperationCreateAPIView.as_view(), name='create_operation'),
    path('api/operation/', OperationListView.as_view(), name='operation-list'),
    
    path('api/create-medicinedosage/', MedicineDosageCreateAPIView.as_view(), name='create_medicinedosage'),
    path('api/medicinedosage/', MedicineDosageListView.as_view(), name='medicinedosage-list'),

    path('api/create-dosageinterval/', DosageIntervalCreateAPIView.as_view(), name='create_dosageinterval'),
    path('api/dosageinterval/', DosageIntervalListView.as_view(), name='dosageinterval-list'),
    
    path('api/create-dosageduration/', DosageDurationCreateAPIView.as_view(), name='create_dosageduration'),
    path('api/dosageduration/', DosageDurationListView.as_view(), name='dosageduration-list'),
    
    path('api/create-pathologycategory/', PathologyCategoryCreateAPIView.as_view(), name='create_pathologycategory'),
    path('api/pathologycategory/', PathologyCategoryListView.as_view(), name='pathologycategory-list'),

    path('api/create-pathologyunit/', PathologyUnitCreateAPIView.as_view(), name='create_pathologyunit'),
    path('api/pathologyunit/', PathologyUnitListView.as_view(), name='pathologyunit-list'),
    
    path('api/create-pathologyparameter/', PathologyParameterCreateAPIView.as_view(), name='create_pathologyparameter'),
    path('api/pathologyparameter/', PathologyParameterListView.as_view(), name='pathologyparameter-list'),
    
    path('api/create-radiologycategory/', RadiologyCategoryCreateAPIView.as_view(), name='create_radiologycategory'),
    path('api/radiologycategory/', RadiologyCategoryListView.as_view(), name='radiologycategory-list'),

    path('api/create-radiologyunit/', RadiologyUnitCreateAPIView.as_view(), name='create_radiologyunit'),
    path('api/radiologyunit/', RadiologyUnitListView.as_view(), name='radiologyunit-list'),
    
    path('api/create-radiologyparameter/', RadiologyParameterCreateAPIView.as_view(), name='create_radiologyparameter'),
    path('api/radiologyparameter/', RadiologyParameterListView.as_view(), name='radiologyparameter-list'),
    
    path('api/create-bloodbankproducts/', BloodBankProductCreateAPIView.as_view(), name='create_bloodbankproducts'),
    path('api/bloodbankproducts/', BloodBankProductListView.as_view(), name='bloodbankproducts-list'),
    
    path('api/create-symptomstype/', SymptomsTypeCreateAPIView.as_view(), name='create_symptomstype'),
    path('api/symptomstype/', SymptomsTypeListView.as_view(), name='symptomstype-list'),
    
    path('api/create-symptomshead/', SymptomsHeadCreateAPIView.as_view(), name='create_symptomshead'),
    path('api/symptomshead/', SymptomsHeadListView.as_view(), name='symptomshead-list'),
    
    path('api/create-findingcategory/', FindingCategoryCreateAPIView.as_view(), name='create_findingcategory'),
    path('api/findingcategory/', FindingCategoryListView.as_view(), name='findingcategory-list'),
    
    path('api/create-finding/', FindingCreateAPIView.as_view(), name='create_finding'),
    path('api/finding/', FindingListView.as_view(), name='finding-list'),
    
    path('api/create-incomehead/', IncomeHeadCreateAPIView.as_view(), name='create_incomehead'),
    path('api/incomehead/', IncomeHeadListView.as_view(), name='incomehead-list'),
    
    path('api/create-expensehead/', ExpenseHeadCreateAPIView.as_view(), name='create_expensehead'),
    path('api/expensehead/', ExpenseHeadListView.as_view(), name='expensehead-list'),
    
    path('api/create-leavetype/', LeaveTypeCreateAPIView.as_view(), name='create_leavetype'),
    path('api/leavetype/', LeaveTypeListView.as_view(), name='leavetype-list'),
    
    path('api/create-department/', DepartmentCreateAPIView.as_view(), name='create_department'),
    path('api/department/', DepartmentListView.as_view(), name='department-list'),
    
    path('api/create-designation/', DesignationCreateAPIView.as_view(), name='create_designation'),
    path('api/designation/', DesignationListView.as_view(), name='designation-list'),
    
    path('api/create-specialist/', SpecialistCreateAPIView.as_view(), name='create_specialist'),
    path('api/specialist/', SpecialistListView.as_view(), name='specialist-list'),
    
    path('api/create-referralcategory/', ReferralCategoryCreateAPIView.as_view(), name='create_referralcategory'),
    path('api/referralcategory/', ReferralCategoryListView.as_view(), name='referralcategory-list'),
    
    path('api/create-referralcommission/', ReferralCommissionCreateAPIView.as_view(), name='create_referralcommission'),
    path('api/referralcommission/', ReferralCommissionListView.as_view(), name='referralcommission-list'),
    
    path('api/create-shift/', ShiftCreateAPIView.as_view(), name='create_shift'),
    path('api/shift/', ShiftListView.as_view(), name='shift-list'),
    
    path('api/create-itemcategory/', ItemCategoryCreateAPIView.as_view(), name='create_itemcategory'),
    path('api/itemcategory/', ItemCategoryListView.as_view(), name='itemcategory-list'),
    
    path('api/create-itemstore/', ItemStoreCreateAPIView.as_view(), name='create_itemstore'),
    path('api/itemstore/', ItemStoreListView.as_view(), name='itemstore-list'),
    
    path('api/create-itemsupplier/', ItemSupplierCreateAPIView.as_view(), name='create_itemsupplier'),
    path('api/itemsupplier/', ItemSupplierListView.as_view(), name='itemsupplier-list'),
    
]
