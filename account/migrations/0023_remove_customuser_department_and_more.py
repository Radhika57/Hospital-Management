# Generated by Django 4.0.2 on 2023-08-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_staffleave_remove_customuser_user_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='leaves',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='specialist',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('admin', 'Admin'), ('doctor', 'Doctor'), ('accountant', 'Accountant'), ('receptionist', 'Receptionist'), ('pharmacist', 'Pharmacist'), ('pathologist', 'Pathologist'), ('radiologist', 'Radiologist'), ('patient', 'Patient'), ('user', 'User')], default='user', max_length=20),
        ),
        migrations.DeleteModel(
            name='StaffLeave',
        ),
    ]