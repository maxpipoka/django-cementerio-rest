from django.contrib import admin
from .models import BurialPermit, City, County, Grave, Parcel, Payment, Periodicity, RegistrationOffice, Sector, State, Tax, Taxpayer, Deceased
from .utils.utils import format_date, format_date_with_time

# Register your models here.

@admin.register(Taxpayer)
class TaxpayerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'dni', 'address', 'city_address', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'dni')
    readonly_fields = ['code', 'dni']

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(Deceased)
class DeceasedAdmin(admin.ModelAdmin):
    list_display = ['deceased', 'date_of_death_formated', 'is_child', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('deceased', 'is_child')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    def date_of_death_formated(self, obj):
        return format_date(obj.date_of_death)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'
    date_of_death_formated.short_description = 'F.de Fallecimiento'



@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'country')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'



@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'state')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'county')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(RegistrationOffice)
class RegistrationOfficeAdmin(admin.ModelAdmin):
    list_display = ['registration_office', 'registration_city', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('registration_office', 'registration_city')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(BurialPermit)
class BurialPermitAdmin(admin.ModelAdmin):
    list_display = ['date_in_registration_office_formated', 'presentation_date_formated', 'deceased','presented_by', 'registration_office', 'observations', 'documents', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('date_in_registration_office', 'deceased', 'presented_by', 'registration_office')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    def date_in_registration_office_formated(self, obj):
        return format_date(obj.date_in_registration_office)
    
    def presentation_date_formated(self, obj):
        return format_date(obj.presentation_date)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'
    date_in_registration_office_formated.short_description = 'Fecha de Reg.'
    presentation_date_formated.short_description = 'Fecha de Pres.'


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'zone')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(Periodicity)
class PeriodicityAdmin(admin.ModelAdmin):
    list_display = ['name', 'years_amount', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'years_amount')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['number', 'row', 'sector', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('number', 'row', 'sector')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'


@admin.register(Grave)
class GraveAdmin(admin.ModelAdmin):
    list_display = ['parcel', 'deceased', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('parcel', 'deceased')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone', 'periodicity', 'amount', 'date_from_formated', 'date_until_formated', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('name', 'zone', 'periodicity', 'amount', 'date_from', 'date_until')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    def date_from_formated(self, obj):
        return format_date(obj.date_from)
    
    def date_until_formated(self, obj):
        return format_date(obj.date_until)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'
    date_from_formated.short_description = 'F.Desde'
    date_until_formated.short_description = 'F.Hasta'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'payment_date_formated', 'taxpayer', 'parcel', 'tax', 'surcharge', 'observations1', 'observations2', 'createdAt_formated', 'updatedAt_formated', 'active']
    search_fields = ('receipt_number', 'payment_date', 'deceased', 'taxpayer')

    def createdAt_formated(self, obj):
        return format_date_with_time(obj.createdAt)
    
    def updatedAt_formated(self, obj):
        return format_date_with_time(obj.updatedAt)
    
    def payment_date_formated(self, obj):
        return format_date(obj.payment_date)
    
    createdAt_formated.short_description = 'Creado/a'
    updatedAt_formated.short_description = 'Mod.o/a'
    payment_date_formated.short_description = 'F.Pago'