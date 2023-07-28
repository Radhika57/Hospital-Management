from django.contrib import admin
from .models import *

admin.site.register(UnitType)
admin.site.register(TaxCategory)
admin.site.register(ChargeType)
admin.site.register(ChargeCategory)
admin.site.register(Charges)
admin.site.register(Floor)
admin.site.register(BedType)
admin.site.register(BedGroup)
admin.site.register(Bed)
admin.site.register(Priority)
admin.site.register(Source)
admin.site.register(ComplainType)
admin.site.register(Purpose)