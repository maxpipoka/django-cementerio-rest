from json import JSONDecodeError

from django.http import JsonResponse
from .models import Taxpayer
from rest_framework import viewsets, views, status
from rest_framework import permissions
from .serializers import TaxpayerSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def getTaxpayers(request):
    taxpayers = Taxpayer.objects.all().order_by('id')
    serializer = TaxpayerSerializer(taxpayers, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def saveTaxpayer(request):
    serializer = TaxpayerSerializer(data=request.data)
    
    if serializer.is_valid():

        if (Taxpayer.objects.filter(dni = serializer.data['dni']).exists()):
            return Response({'message': 'Ya se encuentra el dni en la base de datos'})
        
        if not (Taxpayer.objects.filter(dni = serializer.data['dni']).exists()):

            try:
                serializer.save()
                return Response(serializer.data)

            except:
                Response['status'] = 404
                return Response({'message': 'Error saving'})
            


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