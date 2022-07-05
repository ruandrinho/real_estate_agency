# Generated by Django 2.2.24 on 2022-07-02 13:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners_normalized_phonenumner',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]