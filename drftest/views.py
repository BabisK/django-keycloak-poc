from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets

from drftest.models import TestModel
from drftest.serializers import TestModelSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    permission_classes = [permissions.IsAuthenticated]