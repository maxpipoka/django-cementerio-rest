from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import RegistrationOffice
from ..serializers import RegistrationOfficeSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class RegistrationOfficeViewset(viewsets.ModelViewSet):
    queryset = RegistrationOffice.objects.all()
    serializer_class = RegistrationOfficeSerializer