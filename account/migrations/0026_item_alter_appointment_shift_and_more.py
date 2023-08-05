# Generated by Django 4.0.2 on 2023-08-05 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_alter_referralcommission_ambulance_and_more'),
        ('account', '0025_alter_purchasemedicine_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.itemcategory')),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.shift'),
        ),
        migrations.AlterField(
            model_name='blooddonor',
            name='blood_donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.bloodbank_products'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='complain_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.complaintype'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.source'),
        ),
        migrations.AlterField(
            model_name='components',
            name='bag',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='components',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.bloodbank_products'),
        ),
        migrations.AlterField(
            model_name='cryo',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.AlterField(
            model_name='cryodot',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.AlterField(
            model_name='income',
            name='income_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.incomehead'),
        ),
        migrations.AlterField(
            model_name='inpatient',
            name='bed_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.bedgroup'),
        ),
        migrations.AlterField(
            model_name='inpatient',
            name='bed_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.bed'),
        ),
        migrations.AlterField(
            model_name='inpatient',
            name='symptoms_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.symptomstype'),
        ),
        migrations.AlterField(
            model_name='outpatient',
            name='charge_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.chargecategory'),
        ),
        migrations.AlterField(
            model_name='outpatient',
            name='symptoms_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.symptomstype'),
        ),
        migrations.AlterField(
            model_name='pathologytest',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.pathologycategory'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.bloodbank_products'),
        ),
        migrations.AlterField(
            model_name='plasma',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.AlterField(
            model_name='platelets',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.AlterField(
            model_name='redcells',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.AlterField(
            model_name='testparameter',
            name='test_parameter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.pathologyparameter'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.purpose'),
        ),
        migrations.AlterField(
            model_name='whitecells',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.unittype'),
        ),
        migrations.CreateModel(
            name='ReferralPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer_name', models.CharField(max_length=100)),
                ('referrer_contact', models.CharField(max_length=100)),
                ('contact_person_name', models.CharField(max_length=100)),
                ('contact_person_phone', models.CharField(max_length=100)),
                ('commission', models.CharField(editable=False, max_length=100)),
                ('address', models.TextField()),
                ('opd', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ipd', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pharmacy', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('radiology', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pathology', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('bloodbank', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ambulance', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.referralcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('purchase_price', models.FloatField()),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to='images/itemstock/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.item')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.itemcategory')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.itemstore')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.itemsupplier')),
            ],
        ),
    ]