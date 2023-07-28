from django.urls import path, include
from settings.views import *

urlpatterns = [
    path('api/create-unittype/', UnittypeCreateAPIView.as_view(), name='create_unittype'),
    path('api/create-taxcategory/', TaxCategoryCreateAPIView.as_view(), name='create_taxcategory'),
    path('api/create-chargetype/', ChargeTypeCreateAPIView.as_view(), name='create_chargetype'),
    path('api/create-chargecategory/', ChargeCategoryCreateAPIView.as_view(), name='create_chargecategory'),
    path('api/create-charges/', ChargesCreateAPIView.as_view(), name='create_charges'),
    path('api/create-floor/', FloorCreateAPIView.as_view(), name='create_floor'),
    path('api/create-bedtype/', BedTypeCreateAPIView.as_view(), name='create_bedtype'),
    path('api/create-bedgroup/', BedGroupCreateAPIView.as_view(), name='create_bedgroup'),
    path('api/create-bed/', BedCreateAPIView.as_view(), name='create_bed'),
    path('api/create-priority/', PriorityCreateAPIView.as_view(), name='create_priority'),
    path('api/create-source/', SourceCreateAPIView.as_view(), name='create_source'),
    path('api/create-complaintype/', ComplainTypeCreateAPIView.as_view(), name='create_complaintype'),
    path('api/create-purpose/', PurposeCreateAPIView.as_view(), name='create_purpose'),

]