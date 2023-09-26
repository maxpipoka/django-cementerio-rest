from django.contrib import admin
from .models import Taxpayer

# Register your models here.

@admin.register(Taxpayer)
class TaxpayerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'dni', 'adress']
    search_fields = ('name', 'dni')
    readonly_fields = ['code', 'dni']