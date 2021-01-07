from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.auth is not None and request.method == "POST"
        )

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
            or (request.auth is not None and obj.owner == request.user)
        )
