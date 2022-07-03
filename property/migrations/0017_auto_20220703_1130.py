# Generated by Django 2.2.24 on 2022-07-03 06:30

from django.db import migrations


def fill_owners_table(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            full_name=flat.owner_full_name,
            phone_number=flat.owners_phonenumber,
            pure_phone_number=flat.owner_pure_phone
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20220703_1019'),
    ]

    operations = [
        migrations.RunPython(fill_owners_table)
    ]
