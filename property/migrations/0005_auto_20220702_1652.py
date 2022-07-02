# Generated by Django 2.2.24 on 2022-07-02 11:52

from django.db import migrations


def set_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = (flat.construction_year >= 2015)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building_field)
    ]
