"""
Tests IsOwner class
"""


import typing
from dataclasses import dataclass

from django.test import TestCase

from ..models import Exam
from ..permissions import IsOwner


@dataclass
class Request:
    method: str
    user: typing.Optional[str] = None
    test: bool = True

    @property
    def auth(self):
        return self.user


@dataclass
class Obj:
    owner: typing.Optional[str] = None


class IsOwnerTestCase(TestCase):
    """
    Tests IsOwnerClass
    """

    def test_is_owner_object(self):
        isOwner = IsOwner()
        self.assertTrue(isOwner.has_object_permission(Request("GET"), None, Obj()))
        somevariable = isOwner.has_object_permission(Request("POST"), None, Obj())
        self.assertFalse(somevariable)
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

    def test_is_owner(self):
        isOwner = IsOwner()
        self.assertTrue(isOwner.has_permission(Request("GET"), Obj()))
        somevariable = isOwner.has_permission(Request("POST"), Obj())
        self.assertFalse(somevariable)
        self.assertTrue(isOwner.has_permission(Request("POST", "sergi"), Obj()))
        self.assertFalse(isOwner.has_permission(Request("POST"), Obj()))
        self.assertTrue(
            isOwner.has_permission(Request("PATCH", "sergi"), Obj("quimpm"))
        )

        self.assertTrue(isOwner.has_permission(Request("PATCH", "sergi"), Obj("sergi")))
