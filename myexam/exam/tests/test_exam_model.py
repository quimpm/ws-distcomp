import datetime

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from ..models import Exam

# Create your tests here.
class ExamTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up Exam.
        """
        time = datetime.datetime(
            2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        user1 = User.objects.create(
            username="quimpm",
            password="testingquimpm123",
            email="quimpm@gmail.com",
            first_name="Quim",
            last_name="També",
        )
        Exam.objects.create(
            description="Description", date=time, location="St. X number Y", owner=user1
        )

    def test_content(self):
        exam = Exam.objects.get(id=1)
        self.assertEqual("Description", exam.description)
        time = datetime.datetime(
            2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        self.assertEqual(time, exam.date)
        self.assertEqual("St. X number Y", exam.location)
