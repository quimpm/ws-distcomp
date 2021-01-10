from django.shortcuts import render
from grades.models import Grade
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Exam
from .permissions import IsOwner
from .serializers import ExamSerializer


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
        queryset = Grade.objects.filter(exam=exam)
        if not queryset:
            return super().destroy(request, *args, **kwargs)
        return Response(status=403, data="Exam has grades.")  # TODO És forbidden?


class ExamSearchList(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        queryset = Exam.objects.all()
        description = self.request.query_params.get("description", None)
        if description is not None:
            queryset = queryset.filter(description__icontains=description)
        return queryset
