from django.urls import path, include
from settings.views import *

urlpatterns = [
    path('api/create-unittype/', UnittypeCreateAPIView.as_view(), name='create_unittype'),
    path('api/create-taxcategory/', TaxCategoryCreateAPIView.as_view(), name='create_taxcategory'),
    path('api/create-chargetype/', ChargeTypeCreateAPIView.as_view(), name='create_chargetype'),
    path('api/create-chargecategory/', ChargeCategoryCreateAPIView.as_view(), name='create_chargecategory'),
    path('api/create-charges/', ChargesCreateAPIView.as_view(), name='create_charges'),

]