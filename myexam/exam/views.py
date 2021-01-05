from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Exam
from .serializers import ExamSerializer
from .permissions import IsOwner

# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with the exam.
    """

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsOwner]
