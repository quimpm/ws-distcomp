from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Grade
from exam.models import Exam
from .serializers import GradeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsOwnerOfExamGrade

# Create your views here.
class GradeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with the grades
    """

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsOwnerOfExamGrade]

    @action(detail=True, methods=["get"])
    def user(self, request, pk=None):
        queryset = Grade.objects.all()
        queryset = queryset.filter(user=pk)
        serializer = GradeSerializer(queryset, many=True)
        return Response(status=200, data=serializer.data)

    @action(detail=True, methods=["get"])
    def exam(self, request, pk=None):
        queryset = Grade.objects.all()
        queryset = queryset.filter(exam=pk)
        serializer = GradeSerializer(queryset, many=True)
        return Response(status=200, data=serializer.data)