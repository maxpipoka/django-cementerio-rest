from sre_parse import State
from rest_framework import serializers
from .models import BurialPermit, City, County, State, Deceased, Grave, Parcel, Payment, Periodicity, RegistrationOffice, Sector, Tax, Taxpayer


class TaxpayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxpayer
        fields = '__all__'


class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = '__all__'



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RegistrationOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationOffice
        fields = '__all__'


class BurialPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurialPermit
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class PeriodicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodicity
        fields = '__all__'


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class GraveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grave
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'