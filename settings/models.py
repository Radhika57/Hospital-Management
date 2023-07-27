from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class UnitType(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class TaxCategory(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.FloatField()
    
    def __str__(self):
        return self.name
    
class ChargeType(models.Model):
    chargetype = models.CharField(max_length=20)
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