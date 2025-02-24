from rest_framework import serializers
from django.utils.text import slugify
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = AuthorSerializer()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'category', 'tags', 'author', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)
