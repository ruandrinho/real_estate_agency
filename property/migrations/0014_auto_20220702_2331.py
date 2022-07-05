# Generated by Django 2.2.24 on 2022-07-02 18:31

from django.db import migrations
import phonenumbers


def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phonenumber):
            flat.owners_normalized_phonenumner = f'+{parsed_phonenumber.country_code}{parsed_phonenumber.national_number}'
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220702_1819'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber)
    ]