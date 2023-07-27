# Generated by Django 4.0.2 on 2023-07-24 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_blooddonor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platelets', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cryodot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryodot', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plasma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plasma', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Platelets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platelets', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RedCells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redcells', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WhiteCells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whitecells', models.BooleanField(default=False)),
                ('bag', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('unit', models.CharField(choices=[('select', 'Select'), ('ml', 'ML'), ('litter', 'Litter'), ('mm', 'MM'), ('day', 'Day'), ('hour', 'Hour'), ('insurance', 'Insurance'), ('-', '-'), ('mg', 'MG')], default='Select', max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('select', 'Select'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='Select', max_length=20)),
                ('bag', models.CharField(choices=[('select', 'Select'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='Select', max_length=20)),
                ('cryo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.cryo')),
                ('cryodot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.cryodot')),
                ('plasma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.plasma')),
                ('platelets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.platelets')),
                ('redcells', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.redcells')),
                ('whitecells', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.whitecells')),
            ],
        ),
    ]