from sre_parse import State
from rest_framework import serializers
from .models import BurialPermit, City, County, State, Deceased, Grave, Parcel, Payment, Periodicity, RegistrationOffice, Sector, Tax, Taxpayer


# class TaxpayerSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Taxpayer
#         fields = '__all__'

class TaxpayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    dni = serializers.CharField()

    address = serializers.CharField(max_length=150, required=True)
    city_address = serializers.CharField(max_length=50, required=True)
    createdAt = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField(default=True)

    def validate_dni(self, value):
        # Realiza la validación personalizada para el campo 'dni'
        if isinstance(value, str) and value.lower() == 'sd':
            print('Es string --------------------------------------------')
            return value  # Permitir 'sd' como un caso especial

        # Si no es 'sd', intenta convertir a entero y verifica si es un número válido
        try:
            int_value = int(value)
        except ValueError:
            raise serializers.ValidationError('El campo "dni" debe ser un número entero o la cadena "sd".')

        return int_value

    def create(self, validated_data):
        # Si el valor del campo 'dni' es 'sd', asignamos None al campo dni
        if validated_data['dni'].lower() == 'sd':
            validated_data['dni'] = 0

        return Taxpayer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Implementa el método update si es necesario
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.address = validated_data.get('address', instance.address)
        instance.city_address = validated_data.get('city_address', instance.city_address)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


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