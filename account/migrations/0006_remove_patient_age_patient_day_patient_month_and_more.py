# Generated by Django 4.0.2 on 2023-07-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AddField(
            model_name='patient',
            name='day',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='month',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]