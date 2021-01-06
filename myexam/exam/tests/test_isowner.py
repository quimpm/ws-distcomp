"""
Tests IsOwner class
"""


import typing
from dataclasses import dataclass

from django.test import TestCase

from ..models import Exam
from ..permissions import IsOwner


class IsOwnerTestCase(TestCase):
    """
    Tests IsOwnerClass
    """

    def test_is_owner(self):
        @dataclass
        class Request:
            method: str
            user: typing.Optional[str] = None

        @dataclass
        class Obj:
            owner: typing.Optional[str] = None

        isOwner = IsOwner()
        self.assertTrue(isOwner.has_object_permission(Request("GET"), None, Obj()))
        self.assertFalse(isOwner.has_object_permission(Request("POST"), None, Obj()))
        self.assertTrue(
            isOwner.has_object_permission(Request("POST", "sergi"), None, Obj())
        )
        self.assertFalse(isOwner.has_object_permission(Request("POST"), None, Obj()))
        self.assertFalse(
            isOwner.has_object_permission(
                Request("PATCH", "sergi"), None, Obj("quimpm")
            )
        )

        self.assertTrue(
            isOwner.has_object_permission(Request("PATCH", "sergi"), None, Obj("sergi"))
        )