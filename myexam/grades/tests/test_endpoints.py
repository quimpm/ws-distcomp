from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import Grade
from exam.models import Exam
import datetime
import json


class ApiNoLogedTestGrades(APITestCase):
    @classmethod
    def setUp(self):
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
        user_2 = User.objects.create(
            username="quimpm",
            password="complexpass",
            email="quimpm@gmail.com",
            first_name="Macarroni",
            last_name="Diabola",
        )
        self.exam_1 = Exam.objects.create(
            description="Description", date=time, location="London", owner=user_1
        )
        exam_2 = Exam.objects.create(
            description="Description", date=time, location="London", owner=user_2
        )
        Grade.objects.create(exam=self.exam_1, user=user_1, grade=5.0)
        Grade.objects.create(exam=exam_2, user=user_2, grade=4.99)

    def test_get_user(self):
        response = self.client.get("/grades/1/user/")
        self.assertEqual(response.status_code, 200)

    def test_list_grades(self):
        response = list_grades(self.client)
        self.assertEqual(200, response.status_code)

    def test_create_grade(self):
        response = create_grade(self.client, self.exam_1)
        self.assertEqual(401, response.status_code)

    def test_read_grade(self):
        response = read_grade(self.client)
        self.assertEqual(200, response.status_code)

    def test_update_grade(self):
        response = update_grade(self.client)
        self.assertEqual(401, response.status_code)

    def test_patch_grade(self):
        response = patch_grade(self.client)
        self.assertEqual(401, response.status_code)

    def test_delete_grade(self):
        response = delete_grade(self.client)
        self.assertEqual(401, response.status_code)


class ApiCustomEndpointsTestGrades(APITestCase):
    @classmethod
    def setUp(self):
        time = datetime.datetime(
            2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        user_1 = User.objects.create(
            username="user_ONE",
            password="complexpass",
            email="userone@gmail.com",
            first_name="ONEONE",
            last_name="ONEEEEEE",
        )
        user_2 = User.objects.create(
            username="user_TWO",
            password="complexpass",
            email="usertwo@gmail.com",
            first_name="TWOTWO",
            last_name="TWOOOOOO",
        )

        self.exam_1 = Exam.objects.create(
            description="Exam one", date=time, location="London", owner=user_1
        )
        exam_2 = Exam.objects.create(
            description="Exam two", date=time, location="Asturias", owner=user_1
        )
        exam_3 = Exam.objects.create(
            description="Exam three", date=time, location="Asturias", owner=user_2
        )
        Grade.objects.create(exam=self.exam_1, user=user_1, grade=5.0)
        Grade.objects.create(exam=exam_2, user=user_1, grade=9.0)
        Grade.objects.create(exam=exam_3, user=user_2, grade=1.0)

    def test_get_correct_grades_by_user_1(self):
        response = self.client.get("/grades/1/user/")
        self.assertEqual(len(response.data), 2)

        grade_1 = response.data[0]
        grade_2 = response.data[1]

        self.assertEqual(grade_1["user"], 1)
        self.assertEqual(grade_2["user"], 1)
        self.assertEqual(grade_1["exam"], 1)
        self.assertEqual(grade_2["exam"], 2)

        self.assertEqual(response.status_code, 200)

    def test_get_correct_grades_by_user_2(self):
        response = self.client.get("/grades/2/user/")
        self.assertEqual(len(response.data), 1)

        grade_1 = response.data[0]

        self.assertEqual(grade_1["user"], 2)
        self.assertEqual(grade_1["exam"], 3)

        self.assertEqual(response.status_code, 200)


class ApiLoggedTestGrades(APITestCase):
    def setUp(self):
        """
        Sets Up the Exam
        """
        time = datetime.datetime(
            2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
        )
        user_1 = User.objects.create(
            username="user_ONE",
            password="complexpass",
            email="userone@gmail.com",
            first_name="ONEONE",
            last_name="ONEEEEEE",
        )
        user_2 = User.objects.create(
            username="user_TWO",
            password="complexpass",
            email="usertwo@gmail.com",
            first_name="TWOTWO",
            last_name="TWOOOOOO",
        )
        self.exam_1 = Exam.objects.create(
            description="Exam one", date=time, location="London", owner=user_1
        )
        exam_2 = Exam.objects.create(
            description="Exam two", date=time, location="Asturias", owner=user_1
        )
        exam_3 = Exam.objects.create(
            description="Exam three", date=time, location="Asturias", owner=user_2
        )
        Grade.objects.create(exam=self.exam_1, user=user_1, grade=5.0)
        Grade.objects.create(exam=exam_2, user=user_1, grade=9.0)
        Grade.objects.create(exam=exam_3, user=user_2, grade=1.0)
        self.token = Token.objects.create(user=user_1)
        self.login()

    def login(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def logout(self):
        # self.client.credentials()
        self.client.force_authenticate(user=None)

    def test_get_user(self):
        response = self.client.get("/grades/1/user/")
        self.assertEqual(response.status_code, 200)

    def test_list_grades(self):
        response = list_grades(self.client)
        self.assertEqual(200, response.status_code)

    def test_create_grade(self):
        response = create_grade(self.client, self.exam_1)
        self.assertEqual(201, response.status_code)

    def test_create_grade_no_owner(self):
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
        response = self.client.post("/grades/", data)
        self.assertEqual(403, response.status_code)

    def test_read_grade(self):
        response = read_grade(self.client)
        self.assertEqual(200, response.status_code)

    def test_update_grade(self):
        response = update_grade(self.client)
        self.assertEqual(200, response.status_code)

    def test_update_grade_no_owner(self):
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
        grade = Grade.objects.create(exam=different_exam, user=other_user, grade=6.0)
        data = {"grade": 1.5, "exam": different_exam.pk, "user": other_user.pk}
        response = self.client.put("/grades/" + str(grade.pk) + "/", data)
        self.assertEqual(403, response.status_code)

    def test_patch_grade(self):
        response = patch_grade(self.client)
        self.assertEqual(200, response.status_code)

    def test_patch_grade_no_owner(self):
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
        grade = Grade.objects.create(exam=different_exam, user=other_user, grade=6.0)
        data = {"grade": 1.5}
        response = self.client.patch("/grades/" + str(grade.pk) + "/", data)
        self.assertEqual(403, response.status_code)

    def test_delete_grade(self):
        response = delete_grade(self.client)
        self.assertEqual(204, response.status_code)

    def test_delete_grade_no_owner(self):
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
        grade = Grade.objects.create(exam=different_exam, user=other_user, grade=6.0)
        data = {"grade": 1.5}
        response = self.client.delete("/grades/" + str(grade.pk) + "/", data)
        self.assertEqual(403, response.status_code)


def list_grades(client):
    return client.get("/grades/")


def create_grade(client, exam):
    random_user = User.objects.create(
        username="differentuser",
        password="complexpass",
        email="differentuser@gmail.com",
        first_name="Userdif",
        last_name="Erentus",
    )
    time = datetime.datetime(
        2020, 12, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0))
    )
    data = {"grade": 0.1, "exam": exam.pk, "user": random_user.pk}
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
