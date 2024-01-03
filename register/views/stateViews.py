from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import State
from ..serializers import StateSerializer
from ..utils.utils import (isValueExistInDb,
                          isGreaterThanMaximumLength,
                          isLessThanMinimumLength,
                          isDateFuture,
                          isDatePast)

class StateViewset(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer