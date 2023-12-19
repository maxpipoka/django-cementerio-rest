from django.contrib import admin
from .models import BurialPermit, City, County, Grave, Parcel, Payment, Periodicity, RegistrationOffice, Sector, State, Tax, Taxpayer, Deceased

# Register your models here.

@admin.register(Taxpayer)
class TaxpayerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'dni', 'address', 'city_address', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'dni')
    readonly_fields = ['code', 'dni']


@admin.register(Deceased)
class DeceasedAdmin(admin.ModelAdmin):
    list_display = ['deceased', 'date_of_death', 'is_child', 'createdAt', 'updatedAt', 'active']
    search_fields = ('deceased', 'is_child')



@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'country')



@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'state')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'county')


@admin.register(RegistrationOffice)
class RegistrationOfficeAdmin(admin.ModelAdmin):
    list_display = ['registration_office', 'registration_city', 'createdAt', 'updatedAt', 'active']
    search_fields = ('registration_office', 'registration_city')


@admin.register(BurialPermit)
class BurialPermitAdmin(admin.ModelAdmin):
    list_display = ['date_in_registration_office', 'presentation_date', 'deceased','presented_by', 'registration_office', 'observations', 'documents', 'createdAt', 'updatedAt', 'active']
    search_fields = ('date_in_registration_office', 'deceased', 'presented_by', 'registration_office')


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'zone')


@admin.register(Periodicity)
class PeriodicityAdmin(admin.ModelAdmin):
    list_display = ['name', 'years_amount', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'years_amount')


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['number', 'row', 'sector', 'createdAt', 'updatedAt', 'active']
    search_fields = ('number', 'row', 'sector')


@admin.register(Grave)
class GraveAdmin(admin.ModelAdmin):
    list_display = ['parcel', 'deceased', 'createdAt', 'updatedAt', 'active']
    search_fields = ('parcel', 'deceased')

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone', 'periodicity', 'amount', 'date_from', 'date_until', 'createdAt', 'updatedAt', 'active']
    search_fields = ('name', 'zone', 'periodicity', 'amount', 'date_from', 'date_until')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'payment_date', 'taxpayer', 'parcel', 'tax', 'surcharge', 'observations1', 'observations2', 'createdAt', 'updatedAt', 'active']
    search_fields = ('receipt_number', 'payment_date', 'deceased', 'taxpayer')