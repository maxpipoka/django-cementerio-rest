# Generated by Django 4.2.4 on 2023-12-19 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxpayer',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='taxpayer',
            old_name='city_adress',
            new_name='city_address',
        ),
    ]