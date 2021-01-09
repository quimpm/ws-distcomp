from rest_framework import permissions
from exam.models import Exam
import typing


class IsOwnerOfExamGrade(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            exam_pk = request.data.get("exam", None)
            return _if_exam_correct_owner(exam_pk, request)
        return request.auth is not None

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request,
        - so we'll always allow GET, HEAD or OPTIONS requests.
        - Instance must have an attribute named `owner`.
        - user is authenticated and method is POST/create
        """
        return (
            request.method in permissions.SAFE_METHODS
            or (request.auth is not None and request.method == "POST")
            or (request.auth is not None and obj.exam.owner == request.user)
        )


def _if_exam_correct_owner(exam_pk: typing.Optional[str], request):
    if exam_pk is not None:
        exam = Exam.objects.get(pk=int(exam_pk))
        if exam:
            return exam.owner.pk == request.user.pk
    return False
