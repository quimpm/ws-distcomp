import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from exam.models import Exam
from ..models import Grade


class GradesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Sets Up the Grade
        """
        time = datetime.datetime(
            2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        user_1 = User.objects.create(
            username="furnusmicrowavus",
            password="complexpass",
            email="furnace@gmail.com",
            first_name="Linguini",
            last_name="Kitchen",
        )
        exam_1 = Exam.objects.create(
            description="Description", date=time, location="London", owner=user_1
        )
        Grade.objects.create(exam=exam_1, user=user_1, grade=5.0)
    
    def test_content(self):
        grade = Grade.objects.get(id=1)
        self.assertEqual(1, grade.exam.pk)
        self.assertEqual(1, grade.user.pk)
        self.assertEqual(5.0, grade.grade)