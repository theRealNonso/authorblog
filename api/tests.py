from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

import api.models as am
import api.serializers as abs


class ArticleViewSetCRUD(TestCase):
    """Test module for the am.articleMembership viewset"""

    def setUp(self):
        self.client = APIClient()
        test_user_1 = am.Author.objects.create(
            email="test_user_1@author.blog",
            password="bokejjej"
        )
        test_user_2 = am.Author.objects.create(
            email="test_user_2@author.blog"
        )
        test_user_3 = am.Author.objects.create(
            email="test_user_3@author.blog",
            password="test_user_3@author.blog"
        )
        test_article_1 = am.Articles.objects.create(
            author=test_user_1,
            article="test_article_1",
            relaease_date=datetime(year=2018, month=6, day=30),
        )
        test_article_2 = am.Articles.objects.create(
            author=test_user_2,
            article="test_article_3",
            relaease_date=datetime(year=2018, month=6, day=30),
        )
        test_article_3 = am.Articles.objects.create(
            author=test_user_3,
            article="test_article_3",
            relaease_date=datetime(year=2018, month=6, day=30),
        )

    def test_create(self):
        test_article_2 = am.Articles.objects.get(article="test_article_2")
        test_article_3 = am.Articles.objects.get(article="test_article_3")
        test_article_1 = am.Articles.objects.get(article="test_article_1")

        data = {
            "article": "HELLO BOY",
        }

        # anonymous user can't create article
        response = self.client.post(reverse("article-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        user1 = am.Author.objects.get(email="test_user_1@author.blog")
        self.client.force_authenticate(user=user1)
