from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Periodicity
from ..serializers import PeriodicitySerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class PeriodicityViewset(viewsets.ModelViewSet):
    queryset = Periodicity.objects.all()
    serializer_class = PeriodicitySerializer