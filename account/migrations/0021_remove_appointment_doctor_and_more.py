# Generated by Django 4.0.2 on 2023-08-04 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_ambulance_vehicle_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='inpatient',
            name='consultant_doctor',
        ),
        migrations.RemoveField(
            model_name='outpatient',
            name='consultant_doctor',
        ),
    ]