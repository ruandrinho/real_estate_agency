from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
        db_index=True)
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4',
        db_index=True)
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    like = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        blank=True,
        db_index=True,
        related_name='favourite_flats')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    complainant = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Кто жаловался',
        related_name='complaints')
    flat = models.ForeignKey(
        Flat,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Квартира, на которую пожаловались',
        related_name='complaints')
    text = models.TextField(verbose_name='Текст жалобы')

    def __str__(self):
        return f'{self.complainant.username}, {self.flat.address}'


class Owner(models.Model):
    full_name = models.CharField(
        'ФИО владельца', max_length=200, db_index=True)
    phone_number = models.CharField('Номер владельца', max_length=20)
    pure_phone_number = PhoneNumberField(
        'Нормализованный номер владельца', blank=True, max_length=20)
    flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        blank=True,
        related_name='owners')

    def __str__(self):
        return self.full_name
