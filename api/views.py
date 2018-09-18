import api.serializers as abs
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
import api.models as am
from rest_framework import status
import api.permissions as ap


class ArticleViewset(viewsets.ModelViewSet):
    permission_classes = [ap.ArticleUpdatePermission]
    serializer_class = abs.ArticlesSerializer
    queryset = am.Articles.objects.all()

    def create(self, request, format=None):
        serializer = abs.ArticlesSerializer(data=request.data,
                                            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
