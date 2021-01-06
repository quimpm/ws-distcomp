from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Grade
from .serializers import GradeSerializer

# Create your views here.
class GradeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with the grades
    """

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
