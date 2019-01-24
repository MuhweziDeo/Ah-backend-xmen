from rest_framework import serializers
from .models import Article, ArticleLikes
from authors.apps.profiles.models import Profile
from authors.apps.profiles.serializers import UserProfileSerializer
from authors.apps.utils.estimator import article_read_time
from authors.apps.utils.share_links import share_links_generator
from django.urls import reverse


class AuthorProfileSerializer(UserProfileSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'username', 'image', 'following', )


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorProfileSerializer(read_only=True)
    read_time = serializers.SerializerMethodField()
    share_links = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title', 'slug', 'description', 'created_at',
                  'updated_at', 'favorited', 'favoritesCount',
                  'body', 'image', 'author', 'read_time', 'share_links',
                  'likes_count', 'dislikes_count')

    def get_read_time(self, obj):
        return article_read_time(obj.body)

    def get_author(self, obj):
        return obj.author.id

    def get_share_links(self, obj):
        return share_links_generator(obj, self.context['request'])


class ArticleUpdateSerializer(serializers.ModelSerializer):
    author = AuthorProfileSerializer(read_only=True)
    read_time = serializers.SerializerMethodField()
    share_links = serializers.SerializerMethodField()

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
            'author',
            'read_time',
            'share_links',
            'likes_count',
            'dislikes_count'
        ]

    def get_read_time(self, obj):
        return article_read_time(obj.body)

    def get_share_links(self, obj):
        return share_links_generator(obj, self.context['request'])
