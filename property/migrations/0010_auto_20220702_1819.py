# Generated by Django 2.2.24 on 2022-07-02 13:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owners_normalized_phonenumner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
