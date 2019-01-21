from rest_framework import serializers
from .models import Article
from authors.apps.profiles.models import Profile
from authors.apps.profiles.serializers import UserProfileSerializer


class AuthorProfileSerializer(UserProfileSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'username', 'image', 'following', )


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorProfileSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'slug', 'description', 'created_at',
                  'updated_at', 'favorited', 'favoritesCount',
                  'body', 'image', 'author')


class ArticleUpdateSerializer(serializers.ModelSerializer):
    author = AuthorProfileSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'body',
            'created_at',
            'updated_at',
            'favorited',
            'favoritesCount',
            'image',
            'author'
        ]