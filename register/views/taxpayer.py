from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Taxpayer
from ..serializers import TaxpayerSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class TaxpayerViewset(viewsets.ModelViewSet):
    queryset = Taxpayer.objects.all()
    serializer_class = TaxpayerSerializer

    def create(self, request, *args, **kwargs):
        # Lógica personalizada para el método POST (Crear)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if isValueExistInDb(Taxpayer, {'dni': int(serializer.validated_data['dni'])}):
                message = {'message': 'El dni ya se encuentra registrado'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isValueExistInDb(Taxpayer, {'code': int(serializer.validated_data['code'])}):
                message = {'message': 'El código ya se encuentra registrado'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['name']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['address']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['city_address']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.active = False
        instance.save()
        message = 'Contribuyente desactivado'
        return Response(message, status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            if isValueExistInDb(Taxpayer, {'dni': int(serializer.validated_data['dni'])}):
                message = {'message': 'El dni ya se encuentra registrado'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isValueExistInDb(Taxpayer, {'code': int(serializer.validated_data['code'])}):
                message = {'message': 'El código ya se encuentra registrado'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['name']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['address']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if isLessThanMinimumLength(5, serializer.validated_data['city_address']):
                message = {
                    'message': 'El nombre no tiene al menos 5 caracteres'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

        message= 'Contribuyente actualizado'
        return Response(message, status=status.HTTP_200_OK)