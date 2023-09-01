from rest_framework import serializers
from .models import Taxpayer


class TaxpayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxpayer
        fields = '__all__'