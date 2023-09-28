from datetime import date
from json import JSONDecodeError

from django.http import JsonResponse
from .models import Taxpayer
from rest_framework import viewsets, views, status
from rest_framework import permissions
from .serializers import TaxpayerSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

# VALIDATIONS

def isValueExistInDb(modelToCheck, filter_to_arg = dict) -> bool:
    """ Checks if a value exists in the database 
    Args:
        modelToCheck: The model to check
        filter_to_arg: a dict with a key and value to check if exist in the DDBB

    Returns:
        A boolean indicating if the value exists in the DDBB
    """

    return modelToCheck.objects.filter(**filter_to_arg).exists()
    
def checkMaximunLength(length = int, toCheck = str) -> bool:
    """Validate the contraint of maximun length of a value
    Args:
        length: a int value of a lengt to compare
        toCheck: a string to evaluate its length

    Returns:
        A boolean indicating if string length is under de maximun
    
    """


def checkMinimunLength(length = int, toCheck = str) -> bool:
    """Validate the contraint of minimun length of a value
    
    Args:
        length: a int value of a lengt to compare
        toCheck: a string to evaluate its length

    Returns:
        A boolean indicating if string length is up of the minimum
    
    """
    
    return len(toCheck) < length


def isDateFuture(date_to_check = date) -> bool:
    """Validate that a date is not future of today
    
    Args:
        date_to_check: a date value to compare with the today date

    Returns:
        A boolean indicating if the date is future of today
    """
    
    return date_to_check > (date.today().strftime("%d/%m/%Y"))

def isDatePast(date_to_check = date) -> bool:
    """Validate that a date is not today or the future
    
    Args:
        date_to_check: a date value to compare with the today date

    Returns:
        A boolean indicating if the date is future of today"""
    
    return date_to_check > (date.today().strftime("%d/%m/%Y"))

# Create your views here.

# Endpoint to get all the Taxpayers
@api_view(['GET'])
def getTaxpayers(request):
    try:
        taxpayers = Taxpayer.objects.all().order_by('id')
    except:
        return Response({'message': 'No se pudo acceder a los Contribuyentes'}, status= status.HTTP_204_NO_CONTENT)
        
    serializer = TaxpayerSerializer(taxpayers, many = True)

    return Response(serializer.data)

# Endpoint to save a new Taxpayer
@api_view(['POST'])
def addTaxpayer(request):
    serializer = TaxpayerSerializer(data=request.data)
    
    if serializer.is_valid():
        if (isValueExistInDb(Taxpayer, {'dni': int(serializer.data['dni'])})):
            return Response({'message': 'Ya se encuentra el DNI en la base de datos'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (isValueExistInDb(Taxpayer, {'code': int(serializer.data['code'])})):
            return Response({'message': 'Ya se encuentra el Código en la base de datos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({'message': 'Error saving'}, status=status.HTTP_400_BAD_REQUEST)
        

# Endpoint to edit a Taxpayer
@api_view(['PATCH'])
def editTaxpayer(request):
    serializer = TaxpayerSerializer(data = request.data)

    if serializer.is_valid():
        try:
            taxpayerToEdit = Taxpayer.objects.filter(id == serializer.data['id'])
        except:
            return Response({'message': 'No se encuentra el contribuyente solicitado.',}, status=status.HTTP_400_BAD_REQUEST)


# class TaxpayerViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that allows Taxpayers to be viewed or edited.
#     """

#     queryset = Taxpayer.objects.all()
#     serializer_class = TaxpayerSerializer
#     permission_classes = [permissions.AllowAny]



# class TaxpayerApiView(views.APIView):
#     """
#     A simple APIView for creating contact entires.
#     """

#     def get(self, request):
#         query = Taxpayer.objects.all()
#         serializer_class = TaxpayerSerializer

#         return Response(query)




    # serializer_class = TaxpayerSerializer


    # def get(self):
    #     return Response('texto')
    

    # def get_serializer_context(self):
    #     return {
    #         'request': self.request,
    #         'format': self.format_kwarg,
    #         'view': self
    #     }

    # def get_serializer(self, *args, **kwargs):
    #     kwargs['context'] = self.get_serializer_context()
    #     return self.serializer_class(*args, **kwargs)

    # def post(self, request):
    #     try:
    #         data = JSONParser().parse(request)
    #         serializer = TaxpayerSerializer(data=data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except JSONDecodeError:
    #         return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)