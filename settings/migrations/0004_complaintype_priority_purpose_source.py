# Generated by Django 4.0.2 on 2023-07-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_bedtype_floor_bedgroup_bed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_type', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
