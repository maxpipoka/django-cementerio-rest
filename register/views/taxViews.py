from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Tax
from ..serializers import TaxSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class TaxViewset(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer