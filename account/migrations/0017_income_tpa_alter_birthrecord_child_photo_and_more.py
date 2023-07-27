# Generated by Django 4.0.2 on 2023-07-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_birthrecord_complain_deathrecord_dispatch_receive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_head', models.CharField(choices=[('select', 'Select'), ('hospital charges', 'Hospital Charges'), ('special campaign', 'Special Campaign'), ('canteen rent', 'Canteen Rent'), ('vehicle stand charges', 'Vehicle Stand Charges')], default='Select', max_length=60)),
                ('name', models.CharField(max_length=100)),
                ('invoice_number', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('document', models.ImageField(upload_to='images/income/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=40)),
                ('contact_no', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('contact_person_name', models.CharField(max_length=40)),
                ('contact_person_phone', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='birthrecord',
            name='child_photo',
            field=models.ImageField(upload_to='images/birthrecord/child/'),
        ),
        migrations.AlterField(
            model_name='birthrecord',
            name='document_photo',
            field=models.ImageField(upload_to='images/birthrecord/document/'),
        ),
        migrations.AlterField(
            model_name='birthrecord',
            name='father_photo',
            field=models.ImageField(upload_to='images/birthrecord/father/'),
        ),
        migrations.AlterField(
            model_name='birthrecord',
            name='mother_photo',
            field=models.ImageField(upload_to='images/birthrecord/mother/'),
        ),
        migrations.AlterField(
            model_name='deathrecord',
            name='attachment',
            field=models.ImageField(upload_to='images/deathrecord/'),
        ),
    ]
