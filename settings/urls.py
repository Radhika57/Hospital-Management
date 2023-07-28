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
    

]