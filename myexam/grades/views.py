from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Grade
from .serializers import GradeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class GradeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with the grades
    """

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    @action(detail=True, methods=["get"])
    def user_grades(self, request, pk=None):
        queryset = Grade.objects.all()
        queryset = queryset.filter(user=pk)
        serializer = GradeSerializer(queryset, many=True)
        return Response(status=200, data=serializer.data)
