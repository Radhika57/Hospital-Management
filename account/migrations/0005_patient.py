# Generated by Django 4.0.2 on 2023-07-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_user_type_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('guardian_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('select', 'Select'), ('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], default='Select', max_length=20)),
                ('date_of_birth', models.DateField()),
                ('age', models.DateField()),
                ('blood_group', models.CharField(choices=[('select', 'Select'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='Select', max_length=10)),
                ('marital_status', models.CharField(choices=[('select', 'Select'), ('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('not specified', 'Not Specified')], default='Select', max_length=20)),
                ('patient_image', models.ImageField(upload_to='images/patient/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
                ('allergies', models.TextField()),
                ('tpa_id', models.CharField(max_length=50)),
                ('tpa_validity', models.DateField()),
                ('identify_number', models.CharField(max_length=30)),
                ('alternate_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
