# Generated by Django 2.2.24 on 2022-07-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_auto_20220705_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='likes',
            new_name='users_who_liked',
        ),
    ]
