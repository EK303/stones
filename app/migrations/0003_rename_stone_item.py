# Generated by Django 4.2 on 2023-04-20 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_transaction_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stone',
            new_name='Item',
        ),
    ]
