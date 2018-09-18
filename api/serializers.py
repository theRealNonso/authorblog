from rest_framework import serializers
import api.models as am


###############################################################################
# User management and registration
###############################################################################


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = am.AppUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'bio',
            'date'
        )

    def create(self, validated_data):
        author = am.Author.objects.create_user(**validated_data)
        return author

###############################################################################
# Author blog
###############################################################################


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Author
        fields = (
            'url',
            'username'
        )
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Articles
        fields = '__all__'
        ordering = ('date', )
