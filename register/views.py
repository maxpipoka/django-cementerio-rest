from .models import Taxpayer
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaxpayerSerializer


# Create your views here.

class TaxpayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Taxpayers to be viewed or edited.
    """

    queryset = Taxpayer.objects.all()
    serializer_class = TaxpayerSerializer
    permission_classes = [permissions.IsAuthenticated]