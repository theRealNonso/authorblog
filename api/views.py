import api.serializers as abs
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
import api.models as am
from rest_framework import status
import api.permissions as ap
from rest_framework import permissions


class ArticleViewset(viewsets.ModelViewSet):
    """
    RO:
        can be done by an auth user
    """
    permission_classes = [ap.UpdatePermission]
    serializer_class = abs.ArticlesSerializer
    queryset = am.Articles.objects.all()

    def create(self, request, format=None):
        serializer = abs.ArticlesSerializer(data=request.data,
                                            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewset(viewsets.ModelViewSet):
    """
    Only auth users and owner of the author object
    can update an author,
    creation can only be done by admin
    """

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [ap.UpdatePermission]
        elif self.action == 'create':
            self.permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in self.permission_classes]

    serializer_class = abs.AuthorSerializer
    queryset = am.Author.objects.all()


class GetAuthorArticles(generics.ListAPIView):
    """
    Get only articles related to a particular author,
    passing the id of the author along with the url
    """

    def list(self, request, *args, **kwargs):
        author_id = self.kwargs['id']
        queryset = am.Articles.objects.filter(author=author_id)
        serializer = abs.ArticlesSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
