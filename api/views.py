import api.serializers as abs
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
import api.models as am
from rest_framework import permissions
import api.permissions as ap


class ArticleViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,
                          ap.ArticleUpdatePermission,
                          ap.IsOwner]
    queryset = am.Articles.objects.all()
    serializer_class = abs.ArticlesSerializer

    def get_queryset(self):
        user = self.request.user
        return user.am.Articles.all()

    def create(self, request):
        serializer = abs.ArticlesSerializer
        return Response(serializer.data)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = abs.ArticlesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = am.Articles.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = abs.ArticlesSerializer(article)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = am.Articles.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = abs.ArticlesSerializer(article)
        return Response(serializer.data)
