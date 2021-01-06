from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Exam
from django.utils import timezone
import datetime

class ApiEndpointsTestExam(TestCase):


    @classmethod
    def setUpTestData(cls):
        """
            Sets Up the Exam
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


    def loged_list_exams(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = list_exams(client)
        assert response.status_code == 200
    
    def loged_list_exams_by_description(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = list_exams_by_description(client)
        assert response.status_code == 200

    def loged_create_exam(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = create_exam(client)
        assert response.status_code == 200

    def loged_read_exam(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = read_exam(client)
        assert response.status_code == 200

    def loged_update_exam(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = update_exam(client)
        assert response.status_code == 200


    def loged_partial_update_exam(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        result = partial_update_exam(client)
        assert response.status_code == 200


    def loged_delete_exam(self):
        client = APIClient()
        client.login(username='quimpm', password='testingquimpm123')
        response = delete_exam(client)
        assert response.status_code == 200

    def no_loged_list_exams(self):
        client = APIClient()
        response = list_exams(client)
        assert response.status_code == 401

    def no_loged_create_exam(self):
        client = APIClient()
        response = create_exam(client)
        assert response.status_code == 401

    def no_loged_read_exam(self):
        client = APIClient()
        response = read_exam(client)
        assert response.status_code == 401

    def no_loged_update_exam(self):
        client = APIClient()
        response = update_exam(client)
        assert response.status_code == 401

    def no_loged_partial_update_exam(self):
        client = APIClient()
        response = partial_update_exam(client)
        assert response.status_code == 401

    def no_loged_delete_exam(self):
        client = APIClient()
        response = delete_exam(client)
        assert response.status_code == 401

def list_exams(client):
    return client.get('/exam/')

def list_exams_by_description(client):
    return client.get('/exam/?description=descri')

def create_exam(client):
    time = datetime.datetime(
        2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    data = {
        'description' : 'My heart falls right out of my skiiin',
        'date' : time,
        'location' : 'Carrer Sant Ruf 33, Lleida 25005'
    }
    return client.post('/exam/', data)


def read_exam(client):
    return client.get('/exam/1/')


def update_exam(client):
    time = datetime.datetime(
        2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    data = {
        'description' : 'My heart falls right out of my skiiin',
        'date' : time,
        'location' : 'Carrer Sant Ruf 33, Lleida 25005'
    }
    return client.put('/exam/1', data)


def partial_update_exam(client):
    data = {
        'description' : 'Hola',
    }
    return client.patch('/exam/1/', data)

def delete_exam(client):
    return client.delete('/exam/1/')    