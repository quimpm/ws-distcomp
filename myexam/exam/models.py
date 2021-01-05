from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    """
    Exam Model.

    -> Date is stored as DateField of python
    """

    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="owner"
    )

    def __str__(self):
        return self.description
