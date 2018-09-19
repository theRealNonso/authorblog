from rest_framework import serializers
import api.models as am


###############################################################################
# User management and registration
###############################################################################


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = am.Author
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


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = am.Articles
        fields = '__all__'
        ordering = ('relaease_date', )
