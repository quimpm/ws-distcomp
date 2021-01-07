from django.db import models
from exam.models import Exam
from django.contrib.auth.models import User

# Create your models here.
class Grade(models.Model):
    """
    Grade Model.
    """

    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, null=False, related_name="exam"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="user"
    )
    grade = models.FloatField()

    def __str__(self):
        return f"""Grade(pk={self.pk}, exam={self.exam},
                         user={self.user}
                         grade={self.grade}"""
