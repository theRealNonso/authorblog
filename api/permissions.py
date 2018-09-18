from rest_framework.permissions import BasePermission

import api.models as am


class ArticleUpdatePermission(BasePermission):
    """
    Only creator of author can update article
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsOwner(BasePermission):
    """
    DELETE: user is owner of article
    """

    def has_permission(self, request, view):
        try:
            am.Articles.objects.get(author__pk=view.kwargs["author"],
                                    user=request.user)
        except am.Articles.DoesNotExist:
            return False
        return True
