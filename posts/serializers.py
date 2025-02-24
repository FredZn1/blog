from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comments_count(self, obj):
        return obj.comments.count()
