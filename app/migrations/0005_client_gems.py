# Generated by Django 4.2 on 2023-04-20 15:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='gems',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None),
        ),
    ]
