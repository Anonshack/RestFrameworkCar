# Generated by Django 4.0 on 2021-12-15 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_carowner_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='year of namufacture',
            new_name='year_of_manufacture',
        ),
    ]