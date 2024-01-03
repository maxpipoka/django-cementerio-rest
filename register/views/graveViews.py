from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Grave
from ..serializers import GraveSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class GraveViewset(viewsets.ModelViewSet):
    queryset = Grave.objects.all()
    serializer_class = GraveSerializer