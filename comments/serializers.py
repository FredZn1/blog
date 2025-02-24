from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.replies.count() > 3:
            return "Too many nested replies"
        return CommentSerializer(obj.replies.all(), many=True).data
