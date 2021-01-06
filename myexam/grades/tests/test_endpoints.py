from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Grade
from exam.models import Exam
import datetime


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
            last_name="Kitchen"
        )
        exam_1 = Exam.objects.create(
            description="Description", date=time, location="London", owner=user_1
        )
        Grade.objects.create(
            exam=exam_1, user=user_1, grade=5.0
        )
    
    def test_list_grades(self):
        client = APIClient()
        response = list_grades(client)
        print(response.content)
        assert response.status_code == 200
    
    def test_create_grade(self):
        client = APIClient()
        response = create_grade(client)
        assert response.status_code == 200
    
    def test_read_grade(self):
        client = APIClient()
        response  = read_grade(client)
        assert response.status_code == 200
    
    def test_update_grade(self):
        client = APIClient()
        response = update_grade(client)
        assert response.status_code == 200

    def test_delete_grade(self):
        client = APIClient()
        response = delete_grade(client)
        assert response.status_code == 200


def list_grades(client):
    return client.get('/grades/')

def create_grade(client):
    random_user = User.objects.create(
        username="notateacher",
        password="complexpass",
        email="useruser@gmail.com",
        first_name="Userson",
        last_name="VonUser"
    )
    time = datetime.datetime(
        2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    exam_1 = Exam.objects.create(
            description="Description", date=time, location="London", owner=random_user
    )
    data = {
        "grade": 0.1,
        "exam": exam_1,
        "user": random_user
    }
    print(client.get('/exam/').content)
    return client.post('/grades/',data)

def read_grade(client):
    return client.get('/grades/1/')

def update_grade(client):
    data = {
        "grade": 1.5
    }
    return client.put('/grades/1/', data)

def delete_grade(client):
    return client.delete('/grades/1/')
