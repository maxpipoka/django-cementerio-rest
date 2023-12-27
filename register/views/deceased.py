from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Deceased
from ..serializers import DeceasedSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class DeceasedViewset(viewsets.ModelViewSet):
    queryset = Deceased.objects.all()
    serializer_class = DeceasedSerializer