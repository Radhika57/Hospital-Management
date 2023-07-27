from django.contrib import admin
from .models import *

class TestParameterAdmin(admin.ModelAdmin):
    list_display = ['pathology_test','test_parameter_name','reference_range','unit']

admin.site.register(CustomUser)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(OutPatient)
admin.site.register(InPatient)
admin.site.register(Medicine)
admin.site.register(PathologyTest)
admin.site.register(TestParameter,TestParameterAdmin)
admin.site.register(Platelets)
admin.site.register(Plasma)
admin.site.register(Cryodot)
admin.site.register(WhiteCells)
admin.site.register(RedCells)
admin.site.register(Cryo)
admin.site.register(Components)
admin.site.register(Ambulance)
admin.site.register(Visitor)
admin.site.register(CallLog)
admin.site.register(Receive)
admin.site.register(Dispatch)
admin.site.register(Complain)
admin.site.register(BirthRecord)
admin.site.register(DeathRecord)
admin.site.register(TPA)
admin.site.register(Income)
