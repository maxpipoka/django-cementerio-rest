from django.contrib import admin
from .models import BurialPermit, City, County, Grave, Parcel, Payment, Periodicity, RegistrationOffice, Sector, State, Tax, Taxpayer, Deceased

# Register your models here.

@admin.register(Taxpayer)
class TaxpayerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'dni', 'adress']
    search_fields = ('name', 'dni')
    readonly_fields = ['code', 'dni']


@admin.register(Deceased)
class DeceasedAdmin(admin.ModelAdmin):
    list_display = ['deceased', 'date_of_death', 'is_child']
    search_fields = ('deceased', 'is_child')



@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ('name', 'country')



@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ('name', 'state')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county']
    search_fields = ('name', 'county')


@admin.register(RegistrationOffice)
class RegistrationOfficeAdmin(admin.ModelAdmin):
    list_display = ['registration_office', 'registration_city']
    search_fields = ('registration_office', 'registration_city')


@admin.register(BurialPermit)
class BurialPermitAdmin(admin.ModelAdmin):
    list_display = ['date_in_registration_office', 'presentation_date', 'deceased','presented_by', 'registration_office', 'observations', 'documents']
    search_fields = ('date_in_registration_office', 'deceased', 'presented_by', 'registration_office')


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone']
    search_fields = ('name', 'zone')


@admin.register(Periodicity)
class PeriodicityAdmin(admin.ModelAdmin):
    list_display = ['name', 'years_amount']
    search_fields = ('name', 'years_amount')


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['number', 'row', 'sector']
    search_fields = ('number', 'row', 'sector')


@admin.register(Grave)
class GraveAdmin(admin.ModelAdmin):
    list_display = ['parcel', 'deceased']
    search_fields = ('parcel', 'deceased')

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone', 'periodicity', 'amount', 'date_from', 'date_until']
    search_fields = ('name', 'zone', 'periodicity', 'amount', 'date_from', 'date_until')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'payment_date', 'taxpayer', 'parcel', 'tax', 'surcharge', 'observations1', 'observations2']
    search_fields = ('receipt_number', 'payment_date', 'deceased', 'taxpayer')