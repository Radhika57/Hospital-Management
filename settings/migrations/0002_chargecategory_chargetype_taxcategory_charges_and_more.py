# Generated by Django 4.0.2 on 2023-07-25 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChargeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chargetype', models.CharField(max_length=20)),
                ('appointment', models.BooleanField(default=False)),
                ('OPD', models.BooleanField(default=False)),
                ('IPD', models.BooleanField(default=False)),
                ('pathology', models.BooleanField(default=False)),
                ('radiology', models.BooleanField(default=False)),
                ('blood_bank', models.BooleanField(default=False)),
                ('ambulance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaxCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_name', models.CharField(max_length=100)),
                ('tax', models.FloatField(default=0.0)),
                ('standard_charge', models.FloatField()),
                ('description', models.TextField()),
                ('charge_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.chargecategory')),
                ('charge_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.chargetype')),
                ('tax_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.taxcategory')),
                ('unit_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype')),
            ],
        ),
        migrations.AddField(
            model_name='chargecategory',
            name='charge_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.chargetype'),
        ),
    ]
