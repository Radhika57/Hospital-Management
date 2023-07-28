from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('accountant', 'Accountant'),
        ('receptionist', 'Receptionist'),
        ('pharmacist', 'Pharmacist'),
        ('pathologist', 'Pathologist'),
        ('radiologist', 'Radiologist'),
        ('patient', 'Patient'),
        ('user', 'User')
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='user')
    
    def __str__(self):
        return self.username
 
SHIFT_CHOICES = [
    ('morning', 'Morning'),
    ('evening', 'Evening')
] 

SLOT_CHOICES = [
    ('6:00 AM - 9:00 AM', '6:00 AM - 9:00 AM'),
    ('9:00 AM - 12:00 PM', '9:00 AM - 12:00 PM'),
    ('12:00 PM - 3:00 PM', '12:00 PM - 3:00 PM'),
    ('3:00 PM - 6:00 PM', '3:00 PM - 6:00 PM'),
    ('6:00 PM - 9:00 PM', '6:00 PM - 9:00 PM'),
    ('9:00 PM - 12:00 AM', '9:00 PM - 12:00 AM')  
]

APPOINTMENT_CHOICES = [
    ('normal', 'Normal'),
    ('urgent', 'Urgent'),
    ('very urgent', 'Very Urgent'),
    ('low', 'Low')
]  

PAYMENT_CHOICES = [
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
    ('transfer to bank account', 'Transfer To Bank Account'),
    ('upi', 'UPI'),
    ('other', 'Other'),
    ('online', 'Online')
]  
 
STATUS_CHOICES = [
    ('select', 'Select'),
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('cancel', 'Cancel')
]

CONSULTANT_CHOICES =  [
    ('no', 'No'),
    ('yes', 'Yes')
] 

   
class Appointment(models.Model):
    doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    doctor_fees = models.FloatField(default=200.0)
    shift = models.CharField(max_length=20,choices=SHIFT_CHOICES,default="Select")
    appointment_date = models.DateTimeField(auto_now_add=False,auto_created=False)
    slot = models.CharField(max_length=20,choices=SLOT_CHOICES,default="Select")
    appointment_priority = models.CharField(max_length=20,choices=APPOINTMENT_CHOICES,default="Normal")
    payment_mode = models.CharField(max_length=40,choices=STATUS_CHOICES,default="Select")
    message = models.TextField()
    live_consultant = models.CharField(max_length=10, choices=CONSULTANT_CHOICES,default="Select")
    alternate_address = models.TextField()

    def __str__(self):
        return str(self.id)
 
GENDER_CHOICES = [
    ('select', 'Select'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('transgender', 'Transgender')
]
 
BLOOD_CHOICES = [
    ('select', 'Select'),
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
] 

MARITAL_CHOICES = [
    ('select', 'Select'),
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('separated', 'Separated'),
    ('not specified', 'Not Specified')
]
  
class Patient(models.Model):
    name = models.CharField(max_length=30) 
    guardian_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default="Select")
    date_of_birth = models.DateField(auto_created=False)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=10,choices=BLOOD_CHOICES,default="Select")
    marital_status = models.CharField(max_length=20,choices=MARITAL_CHOICES,default="Select")
    patient_image = models.ImageField(upload_to='images/patient/',null=True,blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    remarks = models.TextField()
    allergies = models.TextField()
    tpa_id = models.CharField(max_length=50)
    tpa_validity = models.DateField(auto_created=False)
    identify_number = models.CharField(max_length=30)
    alternate_number = models.CharField(max_length=20,null=True,blank=True)
    

    @property
    def age(self):
        from datetime import date
        return date(self.year, self.month, self.day)

    @age.setter
    def age(self, value):
        self.year = value.year
        self.month = value.month
        self.day = value.day
    
    def __str__(self):
        return str(self.id)
 
SYMPTOMSTYPE_CHOICES = [
    ('select','Select'),
    ('eating or weight problems','Eating or weight problems'),
    ('emotional problems','Emotional problems'),
    ('muscle or joint problems','Muscle or joint problems'),
    ('skin problems','Skin problems'),
    ('bladder problems','Bladder problems'),
    ('stomach problems','Stomach problems'),
    ('lung problems','Lung problems')
]
 
CASUALTY_CHOICES =  [
    ('no', 'No'),
    ('yes', 'Yes')
] 

OLDPATIENT_CHOICES =  [
    ('no', 'No'),
    ('yes', 'Yes')
] 

CHARGE_CATEGORY_CHOICES = [
    ('select','Select'),
    ('OPD consultaion fees','OPD Consultaion Fees'),
    ('OPD service','OPD Service'),
    ('OPD insurance','OPD Insurance'),
    ('blood pressure check','Blood Pressure Check'),
    ('eye check','Eye Check'),
    ('cholesterol level check','Cholesterol level check'),
    ('sterilization and cleaning equipment','Sterilization and Cleaning Equipment'),
    ('oxygen cylinder','Oxygen cylinder'),
    ('fire extinguisher','Fire extinguisher'),
    ('operation services','Operation Services'),
    ('other charges','Other Charges')
]

class TPA(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    contact_person_name = models.CharField(max_length=40)
    contact_person_phone = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class OutPatient(models.Model):
    # patient_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bp = models.FloatField()
    pulse = models.FloatField()
    temperature = models.FloatField()
    respiration = models.FloatField()
    symptoms_type = models.CharField(max_length=40,choices=SYMPTOMSTYPE_CHOICES,default='select')
    symptoms_title = models.CharField(max_length=100)
    symptoms_description = models.TextField()
    note = models.TextField()
    any_known_allergies = models.TextField()
    previous_medical_issue = models.TextField()
    appointment_date = models.DateTimeField(auto_created=False)
    case = models.CharField(max_length=100)
    casualty = models.CharField(max_length=40,choices=CASUALTY_CHOICES,default='No')
    old_patient = models.CharField(max_length=40,choices=OLDPATIENT_CHOICES,default='No')
    TPA = models.ForeignKey(TPA,on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    consultant_doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    charge_category = models.CharField(max_length=40,choices=CHARGE_CATEGORY_CHOICES,default='Select')
    tax = models.FloatField()
    standard_charge = models.FloatField()
    applied_charge = models.FloatField()
    amount = models.FloatField()
    payment_mode = models.CharField(max_length=30,choices=PAYMENT_CHOICES,default='Cash')
    paid_amount = models.FloatField()
    live_consultation = models.CharField(max_length=30,choices=CONSULTANT_CHOICES,default='No')
    
    def __str__(self):
        return str(self.id)
 
BED_GROUP_CHOICES =[
    ('select','Select'),
    ('VIP ward-ground floor','VIP Ward-Ground Floor'),
    ('Private ward-3rd floor','Private Ward-3rd Floor'),
    ('General ward male-3rd floor','General Ward Male-3rd Floor'),
    ('Private ward-3rd floor','Private Ward-3rd Floor'),
    ('ICU-2nd floor','ICU-2nd Floor'),
    ('NICU-2nd floor','NICU-2nd Floor'),
    ('AC(normal)-1st floor','AC(Normal)-1st Floor'),
    ('Non AC-4th floor','Non AC-4th Floor')
]

BED_NUMBER_CHOICES =[
    ('select','Select')
]
  
class InPatient(models.Model):
    # patient_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bp = models.FloatField()
    pulse = models.FloatField()
    temperature = models.FloatField()
    respiration = models.FloatField()
    symptoms_type = models.CharField(max_length=40,choices=SYMPTOMSTYPE_CHOICES,default='select')
    symptoms_title = models.CharField(max_length=100)
    symptoms_description = models.TextField()
    note = models.TextField()
    previous_medical_issue = models.TextField()
    admission_date = models.DateTimeField(auto_created=False)
    case = models.CharField(max_length=100)
    casualty = models.CharField(max_length=40,choices=CASUALTY_CHOICES,default='No')
    old_patient = models.CharField(max_length=40,choices=OLDPATIENT_CHOICES,default='No')
    TPA = models.ForeignKey(TPA,on_delete=models.CASCADE)
    credit_limit = models.FloatField(default=20000)
    reference = models.CharField(max_length=50)
    consultant_doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bed_group = models.CharField(max_length=40,choices=BED_GROUP_CHOICES,default='Select')
    bed_number = models.CharField(max_length=30,choices=BED_NUMBER_CHOICES,default='Select')
    live_consultation = models.CharField(max_length=30,choices=CONSULTANT_CHOICES,default='No')
    
    def __str__(self):
        return str(self.id)   
 
MEDICINE_CATEGORY_CHOICES = [
    ('select','Select'),
    ('syrup','Syrup'),
    ('capsule','Capsule'),
    ('injection','Injection'),
    ('ointment','Ointment'),
    ('cream','Cream'),
    ('surgical','Surgical'),
    ('drops','Drops'),
    ('inhalers','Inhalers'),
    ('implants/patches','Implants/Patches'),
    ('liquid','Liquid'),
    ('preparations','Preparations'),
    ('diaper','Diaper'),
    ('tablet','Tablet')
]   
    
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_category = models.CharField(max_length=100,choices=MEDICINE_CATEGORY_CHOICES,default='Select')
    medicine_company = models.CharField(max_length=100)
    medicine_composition = models.CharField(max_length=100)
    medicine_group = models.CharField(max_length=100)
    unit = models.PositiveIntegerField()
    min_level = models.PositiveIntegerField()
    re_order_level = models.PositiveIntegerField()
    tax = models.FloatField()
    unit_packing = models.PositiveIntegerField()
    vat_ac = models.CharField(max_length=100)
    note = models.TextField()
    medicine_photo = models.FileField(upload_to='images/medicine/')
    
    def __str__(self):
        return str(self.id)   

PATHOLOGYTEST_CATEGORY_CHOICES = [
    ('select','Select'),
    ('clinical microbiology','Clinical Microbiology'),
    ('clinical chemistry','Clinical Chemistry'),
    ('hematology','Hematology'),
    ('molecular diagnostics','Molecular Diagnostics'),
    ('reproductive biology','Reproductive Biology'),
    ('electromagnetic waves','Electromagnetic Waves'),
]

PATHOLOGYTEST_CHARGE_CHOICES = [
    ('select','Select'),
    ('surgical pathology','Surgical Pathology'),
    ('histopathology','Histopathology'),
    ('cytopathology','Cytopathology'),
    ('forensic pathology','Forensic pathology'),
    ('dermatopathology','Dermatopathology'),
    ('x-ray','X-Ray'),
    ('other charges','Other Charges')
] 

TEST_PARAMETER_CHOICES = [
    ('select','Select'),
    ('rbc','RBC'),
    ('liver function test','Liver Function Test'),
    ('tsh(thyroid stimulation hormone)','TSH(Thyroid Stimulation Hormone)')
]
  
class PathologyTest(models.Model):
    test_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100,choices=PATHOLOGYTEST_CATEGORY_CHOICES,default='Select')
    subcategory = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    report_days = models.PositiveIntegerField()
    charge_category = models.CharField(max_length=100,choices=PATHOLOGYTEST_CHARGE_CHOICES,default='Select')
    tax = models.FloatField(default='30.00' )
    standard_charge = models.FloatField(default='160.00')
    amount = models.FloatField(default='208.00')
    
    def __str__(self):
        return str(self.id)   
    
class TestParameter(models.Model):
    pathology_test = models.ForeignKey(PathologyTest, related_name='parameters', on_delete=models.CASCADE)
    test_parameter_name = models.CharField(max_length=100, choices=TEST_PARAMETER_CHOICES, default='Select')
    reference_range = models.CharField(max_length=40,editable=False)
    unit = models.CharField(max_length=40,editable=False)
    
    def __str__(self):
        return str(self.id)   

    
class BloodDonor(models.Model):
    donor_name = models.CharField(max_length=100)
    d_o_b = models.DateField(auto_created=False)
    blood_donor = models.CharField(max_length=20,choices=BLOOD_CHOICES,default='Select')
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='Select')
    father_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=30)
    address =  models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id) 
 
BAG_CHOICES = [
    ('select','Select'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
]
 
UNIT_CHOICES = [
    ('select','Select'),
    ('ml','ML'),
    ('litter','Litter'),
    ('mm','MM'),
    ('day','Day'),
    ('hour','Hour'),
    ('insurance','Insurance'),
    ('-','-'),
    ('mg','MG'),
]
 
class Platelets(models.Model):
    platelets = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Plasma(models.Model):
    plasma = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Cryodot(models.Model):
    cryodot = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class WhiteCells(models.Model):
    whitecells = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class RedCells(models.Model):
    redcells = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Cryo(models.Model):
    platelets = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.CharField(max_length=20,choices=UNIT_CHOICES,default="Select")
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Components(models.Model):
   blood_group = models.CharField(max_length=20,choices=BLOOD_CHOICES,default='Select')
   bag = models.CharField(max_length=20,choices=BAG_CHOICES,default='Select') 
   platelets = models.ForeignKey(Platelets,on_delete=models.CASCADE)
   plasma = models.ForeignKey(Plasma,on_delete=models.CASCADE)
   cryodot = models.ForeignKey(Cryodot,on_delete=models.CASCADE)
   whitecells = models.ForeignKey(WhiteCells,on_delete=models.CASCADE)
   redcells = models.ForeignKey(RedCells,on_delete=models.CASCADE)
   cryo = models.ForeignKey(Cryo,on_delete=models.CASCADE)
   
   def __str__(self):
        return str(self.id)

VEHICLE_CHOICES =[
    ('select','Select'),
    ('owner','Owner'),
    ('contractual','Contractual')
]
    
class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=40)
    vehicle_model = models.CharField(max_length=40)
    year_made = models.CharField(max_length=10)
    driver_name = models.CharField(max_length=40)
    driver_license = models.CharField(max_length=40)
    driver_contact = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=40,choices=VEHICLE_CHOICES,default="Select")
    note = models.TextField()
    
    def __str__(self):
        return str(self.id)
 
PURPOSE_CHOICES =[
    ('select','Select'),
    ('visit','Visit'),
    ('enquiry','Enquiry'),
    ('seminar','Seminar')
]

VISIT_CHOICES =[
    ('select','Select'),
    ('staff','Staff'),
    ('opd patient','OPD Patient'),
    ('ipd patient','IPD Patient')
] 

CALL_CHOICES =[
    ('incoming','Incoming'),
    ('outgoing','Outgoing')
]

class Visitor(models.Model):
    purpose = models.CharField(max_length=20,choices=PURPOSE_CHOICES,default="Select")
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    id_card = models.CharField(max_length=40)
    visit_to = models.CharField(max_length=40,choices=VISIT_CHOICES,default="Select")
    related_to = models.CharField(max_length=40)
    number_of_person = models.PositiveIntegerField()
    date = models.DateField(auto_created=False)
    in_time = models.TimeField(auto_created=False)
    out_time = models.TimeField(auto_created=False)
    note = models.TextField()
    document = models.FileField(upload_to='images/visitor/')
    
    def __str__(self):
        return str(self.id)
    
class CallLog(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    description = models.TextField()
    nextdate = models.DateField(auto_created=False)
    call_duration = models.CharField(max_length=40)
    note = models.TextField()
    call_type = models.CharField(max_length=10,choices=CALL_CHOICES)
    
    def __str__(self):
        return str(self.id)
    
class Receive(models.Model):
    from_title = models.CharField(max_length=40)
    reference_no = models.CharField(max_length=40)
    address = models.TextField()
    note = models.TextField()
    to_title = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    document = models.FileField(upload_to='images/postal/receive/')
    
    def __str__(self):
        return str(self.id)
    
class Dispatch(models.Model):
    to_title = models.CharField(max_length=40)
    reference_no = models.CharField(max_length=40)
    address = models.TextField()
    note = models.TextField()
    from_title = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    document = models.FileField(upload_to='images/postal/dispatch/')
    
    def __str__(self):
        return str(self.id)
    
COMPLAIN_CHOICES =[
    ('select','Select'),
    ('food quality','Food Quality'),
    ('hospital services','Hospital Services'),
    ('long wait times','Long Wait Times'),
    ('billing discrepancies','Billing Discrepancies')
]

SOURCE_CHOICES =[
    ('select','Select'),
    ('online advertising','Online Advertising'),
    ('from visitors','From Visitors'),
    ('front office','Front Office')
]

class Complain(models.Model):
    complain_type = models.CharField(max_length=40,choices=COMPLAIN_CHOICES,default="Select")
    source = models.CharField(max_length=20,choices=SOURCE_CHOICES,default="Select")
    complain_by = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    description = models.TextField()
    action_taken = models.CharField(max_length=40)
    assigned = models.CharField(max_length=40)
    note = models.TextField()
    document = models.FileField(upload_to='images/complain/')
    
    def __str__(self):
        return str(self.id)
    
class BirthRecord(models.Model):
    child_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default="Select")
    weight = models.CharField(max_length=40)
    child_photo = models.ImageField(upload_to='images/birthrecord/child/')
    date_of_birth = models.DateTimeField(auto_created=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    case_id = models.CharField(max_length=40)
    mother_name = models.CharField(max_length=40) 
    mother_photo = models.ImageField(upload_to='images/birthrecord/mother/')
    father_name = models.CharField(max_length=40) 
    father_photo = models.ImageField(upload_to='images/birthrecord/father/')
    report = models.TextField()
    document_photo = models.ImageField(upload_to='images/birthrecord/document/')
    
    def __str__(self):
        return str(self.id)
    
class DeathRecord(models.Model):
    case_id = models.CharField(max_length=40)
    patient_name = models.CharField(max_length=40)
    death_date = models.DateTimeField(auto_created=False)
    guardian_name = models.CharField(max_length=40) 
    attachment = models.ImageField(upload_to='images/deathrecord/')
    report = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
 
INCOME_HEAD_CHOICES =[
    ('select','Select'),
    ('hospital charges','Hospital Charges'),
    ('special campaign','Special Campaign'),
    ('canteen rent','Canteen Rent'),
    ('vehicle stand charges','Vehicle Stand Charges')
]
    
class Income(models.Model):
    income_head = models.CharField(max_length=60,choices=INCOME_HEAD_CHOICES,default="Select")
    name = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    amount = models.FloatField()
    document = models.ImageField(upload_to='images/income/')
    description = models.TextField()
    
    def __str__(self):
        return str(self.id)