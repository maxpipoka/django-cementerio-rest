from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import BurialPermit
from ..serializers import BurialPermitSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class BurialPermitViewset(viewsets.ModelViewSet):
    queryset = BurialPermit.objects.all()
    serializer_class = BurialPermitSerializer