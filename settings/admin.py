from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UnitType)
admin.site.register(TaxCategory)
admin.site.register(ChargeType)
admin.site.register(ChargeCategory)
admin.site.register(Charges)