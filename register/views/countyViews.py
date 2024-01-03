from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import County
from ..serializers import CountySerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class CountyViewset(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer