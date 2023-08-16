from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from colorfield.fields import ColorField

class UnitType(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class TaxCategory(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.FloatField()
    
    def __str__(self):
        return self.name
    
class ChargeType(models.Model):
    chargetype = models.CharField(max_length=50)
    appointment = models.BooleanField(default=False)
    OPD = models.BooleanField(default=False)
    IPD = models.BooleanField(default=False)
    pathology = models.BooleanField(default=False)
    radiology = models.BooleanField(default=False)
    blood_bank = models.BooleanField(default=False)
    ambulance = models.BooleanField(default=False)
    
    def __str__(self):
        return self.chargetype
    
class ChargeCategory(models.Model):
    charge_type = models.ForeignKey(ChargeType,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Charges(models.Model):
    charge_type = models.ForeignKey(ChargeType,on_delete=models.CASCADE)
    charge_category = models.ForeignKey(ChargeCategory,on_delete=models.CASCADE)
    unit_type = models.ForeignKey(UnitType,on_delete=models.CASCADE)
    charge_name = models.CharField(max_length=100)
    tax_category = models.ForeignKey(TaxCategory,on_delete=models.CASCADE)
    tax = models.FloatField(default=0.0)
    standard_charge = models.FloatField()
    description = models.TextField()
    
    def __str__(self):
        return self.charge_name


@receiver(pre_save, sender=Charges)
def update_tax_percentage(sender, instance, **kwargs):
    # Check if there is a valid tax_category selected
    if instance.tax_category:
        # Get the tax percentage from the related TaxCategory instance
        tax_percentage = instance.tax_category.percentage
        # Update the tax field with the retrieved tax percentage
        instance.tax = tax_percentage 
        
class Floor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class BedGroup(models.Model):
    name = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    color = ColorField(default='#000000')   
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}-{self.floor}"
    
class BedType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Bed(models.Model):
    name = models.CharField(max_length=50)
    bed_type = models.ForeignKey(BedType,on_delete=models.CASCADE)
    bed_group = models.ForeignKey(BedGroup,on_delete=models.CASCADE)
    unused = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Source(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class ComplainType(models.Model):
    complain_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.complain_type
    
class Purpose(models.Model):
    purpose = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.purpose
    
class OperationCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Operation(models.Model):
    operation_name = models.CharField(max_length=50)
    category = models.ForeignKey(OperationCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.operation_name
    
class MedicineCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
class MedicineSupplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_contact = models.CharField(max_length=20)
    contact_person_name = models.CharField(max_length=50)
    contact_person_phone = models.CharField(max_length=20)
    drug_license_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier_name

    
class MedicineDosage (models.Model):
    medicine_category = models.ForeignKey(MedicineCategory,on_delete=models.CASCADE)
    dose = models.CharField(max_length=100)
    unit = models.ForeignKey(UnitType,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dose
    
class DosageInterval(models.Model):
    interval = models.CharField(max_length=50)

    def __str__(self):
        return self.interval
    
class DosageDuration(models.Model):
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.duration
    
class PathologyCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class PathologyUnit(models.Model):
    unit_name = models.CharField(max_length=20)

    def __str__(self):
        return self.unit_name
    
class PathologyParameter(models.Model):
    parameter_name = models.CharField(max_length=100)
    referange_range = models.CharField(max_length=100)
    unit = models.ForeignKey(PathologyUnit,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.parameter_name
    
class RadiologyCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class RadiologyUnit(models.Model):
    unit_name = models.CharField(max_length=20)

    def __str__(self):
        return self.unit_name
    
class RadiologyParameter(models.Model):
    parameter_name = models.CharField(max_length=100)
    referange_range = models.CharField(max_length=100)
    unit = models.ForeignKey(RadiologyUnit,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.parameter_name

class BloodBank_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BloodBank_Products(models.Model):
    types = models.ForeignKey(BloodBank_Type,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
class SymptomsType(models.Model):
    symptoms_type = models.CharField(max_length=100)

    def __str__(self):
        return self.symptoms_type
    
class SymptomsHead(models.Model):
    symptoms_head = models.CharField(max_length=100)
    symptoms_type = models.ForeignKey(SymptomsType,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.symptoms_head
    
class FindingCategory(models.Model):
    finding_category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.finding_category
    
class Finding(models.Model):
    finding = models.CharField(max_length=100)
    category = models.ForeignKey(FindingCategory,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.finding
    
class IncomeHead(models.Model):
    income_head = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.income_head
    
class ExpenseHead(models.Model):
    expense_head = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.expense_head
    
class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.leave_type
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Specialist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ReferralCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ReferralCommission(models.Model):
    category = models.ForeignKey(ReferralCategory, on_delete=models.CASCADE)
    standard_commission = models.CharField(max_length=100)
    opd = models.CharField(max_length=100, null=True, blank=True, default=None)
    ipd = models.CharField(max_length=100, null=True, blank=True, default=None)
    pharmacy = models.CharField(max_length=100, null=True, blank=True, default=None)
    radiology = models.CharField(max_length=100, null=True, blank=True, default=None)
    pathology = models.CharField(max_length=100, null=True, blank=True, default=None)
    bloodbank = models.CharField(max_length=100, null=True, blank=True, default=None)
    ambulance = models.CharField(max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.category)

    def save(self, *args, **kwargs):
        existing_commission = ReferralCommission.objects.filter(category=self.category).first()

        if existing_commission:
            self.opd = self.opd if self.opd else existing_commission.opd
            self.ipd = self.ipd if self.ipd else existing_commission.ipd
            self.pharmacy = self.pharmacy if self.pharmacy else existing_commission.pharmacy
            self.radiology = self.radiology if self.radiology else existing_commission.radiology
            self.pathology = self.pathology if self.pathology else existing_commission.pathology
            self.bloodbank = self.bloodbank if self.bloodbank else existing_commission.bloodbank
            self.ambulance = self.ambulance if self.ambulance else existing_commission.ambulance

        super(ReferralCommission, self).save(*args, **kwargs)
    
class Shift(models.Model):
    name = models.CharField(max_length=100)
    time_from = models.TimeField(auto_created=False)
    time_to = models.TimeField(auto_created=False)
    
    def __str__(self):
        return f"{self.name} ({self.time_from}-{self.time_to})"
    
class ItemCategory(models.Model):
    item_category = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.item_category
    
class ItemStore(models.Model):
    item_store_name = models.CharField(max_length=100)
    item_store_code = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.item_store_name
    
class ItemSupplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_person_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=100)
    contact_person_email = models.EmailField(unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
