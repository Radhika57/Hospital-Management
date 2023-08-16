from django.db import models
from django.contrib.auth.models import AbstractUser
from settings.models import *

USER_TYPES = [
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
]

DESIGNATION_CHOICES = [
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
        ('it admin', 'IT Admin'),
        ('pathologist', 'Pathologist'),
        ('pharmacist', 'Pharmacist'),
        ('radiologist', 'Radiologist'),
        ('nurse','Nurse'),
        ('accountant', 'Accountant'),
        ('receptionist', 'Receptionist'),
        ('driver','Driver'),
        ('technical head','Technical Head')
    ]

DEPARTMENT_CHOICES = [
        ('ot', 'OT'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
        ('ipd', 'IPD'),
        ('opd', 'OPD'),
        ('icu', 'ICU'),
        ('blood_bank', 'Blood_Bank'),
        ('pathology', 'Pathology'),
        ('radiology', 'Radiology'),
        ('pharmacy','Pharmacy'),
        ('reception', 'Reception'),
        ('human resource', 'Human Resource'),
        ('gynecology','Gynecology'),
        ('finance','Finance'),
        ('emergency','Emergency'),
        ('cardiology','Cardiology'),
        ('burn care','BURN CARE'),
        ('nicu','NICU'),
        ('nursing department','Nursing Department')
    ]

SPECIALIST_CHOICES = [
    ('cardiologist', 'Cardiologist'),
    ('dermatologists', 'Dermatologists'),
    ('gastroenterologists', 'Gastroenterologists'),
    ('ophthalmologists', 'Ophthalmologists'),
    ('neuroradiology', 'Neuroradiology')
]

GENDER_CHOICES = [
    ('select', 'Select'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('transgender', 'Transgender')
] 

MARITAL_CHOICES = [
    ('select', 'Select'),
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('separated', 'Separated'),
    ('not specified', 'Not Specified')
]  
BLOODGROUP_CHOICES = [
    ('O+','O+'),
    ('A+','A+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('O-','O-'),
    ('A-','A-'),
    ('B-','B-'),
    ('AB-','AB-'),
]

CONTRACT_CHOICES = [
    ('permanent','Permanent'),
    ('probation','Probation')
]

class CustomUser(AbstractUser):
    staff_id = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=20, choices=USER_TYPES, default='user')
    designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICES)
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES)
    specialist = models.CharField(max_length=50,choices=SPECIALIST_CHOICES)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    father_name = models.CharField(max_length=50,null=True,blank=True)
    mother_name = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=50,choices=MARITAL_CHOICES)
    blood_group = models.CharField(max_length=20,choices=BLOODGROUP_CHOICES)
    dob = models.DateField(auto_created=False,null=True,blank=True)
    date_of_joining = models.DateField(auto_created=False,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    emergency_contact = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(unique=True)
    photo = models.FileField(upload_to='images/staff/',null=True,blank=True)
    current_address = models.TextField(null=True,blank=True)
    permanent_address = models.TextField(null=True,blank=True)
    qualification = models.TextField(null=True,blank=True)
    work_experience = models.TextField(null=True,blank=True)
    specialization = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    pan_number = models.CharField(max_length=50,null=True,blank=True)
    national_identification_number = models.CharField(max_length=50,null=True,blank=True)
    local_identification_number = models.CharField(max_length=50,null=True,blank=True)
    reference_contact = models.CharField(max_length=50,null=True,blank=True)
    epf_number = models.CharField(max_length=50,null=True,blank=True)
    basic_salary = models.CharField(max_length=50,null=True,blank=True)
    contract_type = models.CharField(max_length=20,choices=CONTRACT_CHOICES)
    work_shift = models.CharField(max_length=50,null=True,blank=True)
    work_location = models.CharField(max_length=50,null=True,blank=True)
    casual_leave = models.PositiveIntegerField(null=True,blank=True)
    privilege_leave = models.PositiveIntegerField(null=True,blank=True)
    sick_leave = models.PositiveIntegerField(null=True,blank=True)
    maternity_leave = models.PositiveIntegerField(null=True,blank=True)
    paternity_leave = models.PositiveIntegerField(null=True,blank=True)
    fever_leave = models.PositiveIntegerField(null=True,blank=True)
    account_title = models.CharField(max_length=100,null=True,blank=True)
    bank_account_no = models.CharField(max_length=100,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    ifsc_code = models.CharField(max_length=100,null=True,blank=True)
    bank_branch_name = models.CharField(max_length=100,null=True,blank=True)
    facebook_url = models.URLField(null=True,blank=True)
    twitter_url = models.URLField(null=True,blank=True)
    linkedin_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    resume = models.FileField(upload_to='images/staff/resume/',null=True,blank=True)
    joining_letter = models.FileField(upload_to='images/staff/joining_letter',null=True,blank=True)
    other_document = models.FileField(upload_to='images/staff/other_document',null=True,blank=True)
    
    def __str__(self):
        return self.email
 
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
    # doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    doctor_fees = models.FloatField(default=200.0)
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=False,auto_created=False)
    slot = models.CharField(max_length=20,choices=SLOT_CHOICES,default="select")
    appointment_priority = models.CharField(max_length=20,choices=APPOINTMENT_CHOICES,default="normal")
    payment_mode = models.CharField(max_length=40,choices=STATUS_CHOICES,default="select")
    message = models.TextField()
    live_consultant = models.CharField(max_length=10, choices=CONSULTANT_CHOICES,default="select")
    alternate_address = models.TextField()

    def __str__(self):
        return str(self.id)
 
  
class Patient(models.Model):
    name = models.CharField(max_length=30) 
    guardian_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default="select")
    date_of_birth = models.DateField(auto_created=False)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    blood_group = models.ForeignKey(BloodBank_Products,on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=20,choices=MARITAL_CHOICES,default="select")
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
 
CASUALTY_CHOICES =  [
    ('no', 'No'),
    ('yes', 'Yes')
] 

OLDPATIENT_CHOICES =  [
    ('no', 'No'),
    ('yes', 'Yes')
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
    symptoms_type = models.ForeignKey(SymptomsType,on_delete=models.CASCADE)
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
    # consultant_doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    charge_category = models.ForeignKey(ChargeCategory,on_delete=models.CASCADE)
    tax = models.FloatField()
    standard_charge = models.FloatField()
    applied_charge = models.FloatField()
    amount = models.FloatField()
    payment_mode = models.CharField(max_length=30,choices=PAYMENT_CHOICES,default='Cash')
    paid_amount = models.FloatField()
    live_consultation = models.CharField(max_length=30,choices=CONSULTANT_CHOICES,default='No')
    
    def __str__(self):
        return str(self.id)
  
class InPatient(models.Model):
    # patient_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bp = models.FloatField()
    pulse = models.FloatField()
    temperature = models.FloatField()
    respiration = models.FloatField()
    symptoms_type = models.ForeignKey(SymptomsType,on_delete=models.CASCADE)
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
    # consultant_doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bed_group = models.ForeignKey(BedGroup,on_delete=models.CASCADE)
    bed_number = models.ForeignKey(Bed,on_delete=models.CASCADE)
    live_consultation = models.CharField(max_length=30,choices=CONSULTANT_CHOICES,default='No')
    
    def __str__(self):
        return str(self.id)      


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

class PathologyTest(models.Model):
    test_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)
    category_name = models.ForeignKey(PathologyCategory,on_delete=models.CASCADE)
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
    test_parameter_name = models.ForeignKey(PathologyParameter,on_delete=models.CASCADE)
    reference_range = models.CharField(max_length=40,editable=False)
    unit = models.CharField(max_length=40,editable=False)
    
    def __str__(self):
        return str(self.id)   


VEHICLE_CHOICES =[
    ('select','Select'),
    ('owner','Owner'),
    ('contractual','Contractual')
]
    
 
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
    purpose = models.ForeignKey(Purpose,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    id_card = models.CharField(max_length=40)
    visit_to = models.CharField(max_length=40,choices=VISIT_CHOICES,default="select")
    related_to = models.CharField(max_length=40)
    number_of_person = models.PositiveIntegerField()
    date = models.DateField(auto_created=False)
    in_time = models.TimeField(auto_created=False)
    out_time = models.TimeField(auto_created=False)
    note = models.TextField()
    document = models.FileField(null=True , blank=True ,upload_to='images/visitor/')
    
    def __str__(self):
        return str(self.id)
    
##############################################################
    
class Dispatch(models.Model):
    to_title = models.CharField(max_length=40)
    reference_no = models.CharField(max_length=40)
    address = models.TextField()
    note = models.TextField()
    from_title = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    document = models.FileField(null=True , blank=True ,upload_to='images/postal/dispatch/')
    
    def __str__(self):
        return str(self.id)
    
class Receive(models.Model):
    from_title = models.CharField(max_length=40)
    reference_no = models.CharField(max_length=40)
    address = models.TextField()
    note = models.TextField()
    to_title = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    document = models.FileField(null=True , blank=True ,upload_to='images/postal/receive/')
    
    def __str__(self):
        return str(self.id)

class Complain(models.Model):
    complain_type = models.ForeignKey(ComplainType,on_delete=models.CASCADE)
    source = models.ForeignKey(Source,on_delete=models.CASCADE)
    complain_by = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    description = models.TextField()
    action_taken = models.CharField(max_length=40)
    assigned = models.CharField(max_length=40)
    note = models.TextField()
    document = models.FileField(null=True , blank=True ,upload_to='images/complain/')
    
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
    
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_category = models.ForeignKey(MedicineCategory,on_delete=models.CASCADE)
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
    medicine_photo = models.FileField(null=True , blank=True ,upload_to='images/medicine/')
    
    def __str__(self):
        return str(self.medicine_name)
    
class PurchaseMedicine(models.Model):
    medicine_category = models.ForeignKey(MedicineCategory,on_delete=models.CASCADE)
    medicine_name = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=20)
    expiry_date = models.DateField(auto_created=False)
    mrp = models.FloatField()
    batch_amount = models.FloatField()
    sale_price = models.FloatField()
    packing_qty = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    purchase_price = models.FloatField()
    tax = models.PositiveIntegerField(editable=False,null=True)
    amount = models.FloatField()
    
    def __str__(self):
        return str(self.batch_no)
    
class Platelets(models.Model):
    platelets = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Plasma(models.Model):
    plasma = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Cryodot(models.Model):
    cryodot = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class WhiteCells(models.Model):
    whitecells = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class RedCells(models.Model):
    redcells = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Cryo(models.Model):
    platelets = models.BooleanField(default=False)
    bag = models.CharField(max_length=20,null=True,blank=True)
    volume = models.CharField(max_length=20,null=True,blank=True)
    unit = models.ForeignKey(UnitType,on_delete = models.CASCADE)
    lot = models.CharField(max_length=20,null=True,blank=True)
    institution = models.CharField(max_length=200,null=True,blank=True)
    
class Components(models.Model):
   blood_group = models.ForeignKey(BloodBank_Products,on_delete=models.CASCADE)
   bag = models.PositiveIntegerField()
   platelets = models.ForeignKey(Platelets,on_delete=models.CASCADE)
   plasma = models.ForeignKey(Plasma,on_delete=models.CASCADE)
   cryodot = models.ForeignKey(Cryodot,on_delete=models.CASCADE)
   whitecells = models.ForeignKey(WhiteCells,on_delete=models.CASCADE)
   redcells = models.ForeignKey(RedCells,on_delete=models.CASCADE)
   cryo = models.ForeignKey(Cryo,on_delete=models.CASCADE)
   
   def __str__(self):
        return str(self.id)
    
class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=40)
    vehicle_model = models.CharField(max_length=40)
    year_made = models.CharField(max_length=10)
    driver_name = models.CharField(max_length=40)
    driver_license = models.CharField(max_length=40)
    driver_contact = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=40,choices=VEHICLE_CHOICES,default="select")
    note = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class BirthRecord(models.Model):
    child_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default="select")
    weight = models.CharField(max_length=40)
    child_photo = models.ImageField(null=True , blank=True ,upload_to='images/birthrecord/child/')
    date_of_birth = models.DateTimeField(auto_created=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    case_id = models.CharField(max_length=40)
    mother_name = models.CharField(max_length=40) 
    mother_photo = models.ImageField(null=True , blank=True ,upload_to='images/birthrecord/mother/')
    father_name = models.CharField(max_length=40) 
    father_photo = models.ImageField(null=True , blank=True ,upload_to='images/birthrecord/father/')
    report = models.TextField()
    document_photo = models.ImageField(null=True , blank=True ,upload_to='images/birthrecord/document/')
    
    def __str__(self):
        return str(self.id)
    
class DeathRecord(models.Model):
    case_id = models.CharField(max_length=40)
    patient_name = models.CharField(max_length=40)
    death_date = models.DateTimeField(auto_created=False)
    guardian_name = models.CharField(max_length=40) 
    attachment = models.ImageField(null=True , blank=True ,upload_to='images/deathrecord/')
    report = models.TextField()
    
    def __str__(self):
        return str(self.id)

    
class Income(models.Model):
    income_head = models.ForeignKey(IncomeHead,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    amount = models.FloatField()
    document = models.ImageField(null=True , blank=True ,upload_to='images/income/')
    description = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Expense(models.Model):
    expense_head = models.ForeignKey(ExpenseHead,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=40)
    date = models.DateField(auto_created=False)
    amount = models.FloatField()
    document = models.ImageField(null=True , blank=True ,upload_to='images/expense/')
    description = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Item(models.Model):
    item = models.CharField(max_length=100)
    item_category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    unit =  models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return str(self.item)
    
class ItemStock(models.Model):
    item_category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(ItemSupplier,on_delete=models.CASCADE)
    store = models.ForeignKey(ItemStore,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.FloatField()
    date = models.DateField(auto_created=False)
    description = models.TextField()
    document = models.FileField(null=True , blank=True ,upload_to='images/itemstock/')
    
    def __str__(self):
        return str(self.id)

class ReferralPerson(models.Model):
    referrer_name = models.CharField(max_length=100)
    referrer_contact = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=100) 
    category = models.ForeignKey(ReferralCategory,on_delete=models.CASCADE)
    commission = models.CharField(max_length=100)
    address = models.TextField()
    opd = models.CharField(max_length=100, null=True, blank=True, default=None)
    ipd = models.CharField(max_length=100, null=True, blank=True, default=None)
    pharmacy = models.CharField(max_length=100, null=True, blank=True, default=None)
    radiology = models.CharField(max_length=100, null=True, blank=True, default=None)
    pathology = models.CharField(max_length=100, null=True, blank=True, default=None)
    bloodbank = models.CharField(max_length=100, null=True, blank=True, default=None)
    ambulance = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.referrer_name)
    
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

        super(ReferralPerson, self).save(*args, **kwargs)
        
class BloodDonor(models.Model):
    donor_name = models.CharField(max_length=100)
    d_o_b = models.DateField(auto_created=False)
    blood_donor = models.ForeignKey(BloodBank_Products,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='Select')
    father_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=30)
    address =  models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)