from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Parcel
from ..serializers import ParcelSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class ParcelViewset(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer