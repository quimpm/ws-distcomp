from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import Exam
from django.utils import timezone
import datetime


class ApiEndpointsTestExam(APITestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets Up the Exam
        """
        time = datetime.datetime(
            2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        cls.user = User.objects.create(
            username="quimpm",
            password="testingquimpm123",
            email="quimpm@gmail.com",
            first_name="Quim",
            last_name="També",
        )
        Exam.objects.create(
            description="Description",
            date=time,
            location="St. X number Y",
            owner=cls.user,
        )
        cls.token = Token.objects.create(user=cls.user)

    def login(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def logout(self):
        # self.client.credentials()
        self.client.force_authenticate(user=None)

    def test_logged_list_exams(self):
        self.login()
        response = list_exams(self.client)
        self.assertEqual(200, response.status_code)
        self.logout()

    def test_logged_list_exams_by_description(self):
        self.login()
        response = list_exams_by_description(self.client)
        self.assertEqual(200, response.status_code)
        self.logout()

    def test_logged_create_exam(self):
        self.login()
        response = create_exam(self.client)
        self.assertEqual(201, response.status_code)
        self.logout()

    def test_logged_read_exam(self):
        self.login()
        response = read_exam(self.client)
        self.assertEqual(200, response.status_code)
        self.logout()

    def test_logged_update_exam(self):
        self.login()
        response = update_exam(self.client)
        self.assertEqual(200, response.status_code)
        self.logout()

    def test_logged_partial_update_exam(self):
        self.login()
        response = partial_update_exam(self.client)
        self.assertEqual(200, response.status_code)
        self.logout()

    def test_logged_delete_exam(self):
        self.login()
        response = delete_exam(self.client)
        self.assertEqual(204, response.status_code)
        self.logout()

    def test_no_logged_list_exams(self):
        response = list_exams(self.client)
        self.assertEqual(200, response.status_code)

    def test_no_logged_list_exams_by_description(self):
        response = list_exams_by_description(self.client)
        self.assertEqual(200, response.status_code)

    def test_no_logged_create_exam(self):
        response = create_exam(self.client)
        self.assertEqual(403, response.status_code)

    def test_no_logged_read_exam(self):
        response = read_exam(self.client)
        self.assertEqual(200, response.status_code)

    def test_no_logged_update_exam(self):
        response = update_exam(self.client)
        self.assertEqual(403, response.status_code)

    def test_no_logged_partial_update_exam(self):
        response = partial_update_exam(self.client)
        self.assertEqual(403, response.status_code)

    def test_no_logged_delete_exam(self):
        response = delete_exam(self.client)
        self.assertEqual(403, response.status_code)


def list_exams(client):
    return client.get("/exam/")


def list_exams_by_description(client):
    return client.get("/exam/?description=descri")


def create_exam(client):
    time = datetime.datetime(
        2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    owner_1 = User.objects.create(
        username="kimpaema",
        password="testingquimpm123",
        email="quimpm@gmail.com",
        first_name="Quim",
        last_name="També",
    )
    data = {
        "description": "My heart falls right out of my skiiin",
        "date": time,
        "location": "Carrer Sant Ruf 33, Lleida 25005",
        "owner": owner_1.pk,
    }
    return client.post("/exam/", data)


def read_exam(client):
    return client.get("/exam/1/")


def update_exam(client):
    time = datetime.datetime(
        2020, 12, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    owner = User.objects.create(
        username="ticcansatdusernamesja",
        password="testingquimpm123",
        email="quimpm@gmail.com",
        first_name="Quim",
        last_name="També",
    )
    breakpoint()
    data = {
        "description": "My heart falls right out of my skiiin",
        "date": time,
        "location": "Carrer Sant Ruf 33, Lleida 25005",
        "owner": owner.pk,
    }
    return client.put("/exam/1/", data)


def partial_update_exam(client):
    data = {
        "description": "Hola",
    }
    return client.patch("/exam/1/", data)


def delete_exam(client):
    return client.delete("/exam/1/")
