from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Grade
from exam.models import Exam
import datetime
import json


class ApiEndpointsTestGrades(TestCase):
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

    def test_list_grades(self):
        client = APIClient()
        response = list_grades(client)
        self.assertEqual(200, response.status_code)

    def test_create_grade(self):
        client = APIClient()
        response = create_grade(client)
        self.assertEqual(201, response.status_code)

    def test_read_grade(self):
        client = APIClient()
        response = read_grade(client)
        self.assertEqual(200, response.status_code)

    def test_update_grade(self):
        client = APIClient()
        response = update_grade(client)
        self.assertEqual(200, response.status_code)

    def test_patch_grade(self):
        client = APIClient()
        response = patch_grade(client)
        self.assertEqual(200, response.status_code)

    def test_delete_grade(self):
        client = APIClient()
        response = delete_grade(client)
        self.assertEqual(204, response.status_code)


def list_grades(client):
    return client.get("/grades/")


def create_grade(client):
    random_user = User.objects.create(
        username="notateacher",
        password="complexpass",
        email="useruser@gmail.com",
        first_name="Userson",
        last_name="VonUser",
    )
    time = datetime.datetime(
        2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    exam_1 = Exam.objects.create(
        description="Description", date=time, location="London", owner=random_user
    )
    data = {"grade": 0.1, "exam": exam_1.pk, "user": random_user.pk}
    return client.post("/grades/", data)


def read_grade(client):
    return client.get("/grades/1/")


def update_grade(client):
    other_user = User.objects.create(
        username="differentuser",
        password="complexpass",
        email="differentuser@gmail.com",
        first_name="Userdif",
        last_name="Erentus",
    )
    time = datetime.datetime(
        2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    different_exam = Exam.objects.create(
        description="This time the exam is in Naples",
        date=time,
        location="Naples",
        owner=other_user,
    )
    data = {"grade": 1.5, "exam": different_exam.pk, "user": other_user.pk}
    return client.put("/grades/1/", data)


def patch_grade(client):
    data = {"grade": 9}
    return client.patch("/grades/1/", data)


def delete_grade(client):
    return client.delete("/grades/1/")
