from django.urls import path
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework.routers import DefaultRouter
import api.views as av

router = DefaultRouter(trailing_slash=False)
app_router = routers.DefaultRouter()
app_router.register(r'article', av.ArticleViewset, 'article')

urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
    path('docs/', include_docs_urls(title='AuthorBlog Backend API',
                                    public=True)),
    path('', include(app_router.urls)),

]
