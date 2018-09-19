from rest_framework.permissions import BasePermission


class UpdatePermission(BasePermission):
    """
    Only creator of author can update article
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user
