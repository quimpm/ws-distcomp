from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Exam
from grades.models import Grade
from .serializers import ExamSerializer
from .permissions import IsOwner
from rest_framework.response import Response

# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with the exam.
    """

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsOwner]

    def destroy(self, request, *args, **kwargs):
        exam = self.get_object().pk
        queryset  = Grade.objects.filter(exam=exam)
        if queryset:
            return super().destroy(request, *args, **kwargs)

        return Response(status=403, data="Exam has grades.") # TODO És forbidden?


class ExamSearchList(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        queryset = Exam.objects.all()
        description = self.request.query_params.get("description", None)
        if description is not None:
            queryset = queryset.filter(description__icontains=description)
        return queryset
