from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.StackedInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('users_who_liked',)
    inlines = [OwnersInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complainant', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
