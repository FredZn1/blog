from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import Comment

class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.__class__(instance, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(many=True, read_only=True)
    author_email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'author_email', 'content', 'parent', 'created_at', 'replies']

    def validate(self, data):
        if data.get('parent'):
            parent = data['parent']
            level = 1
            while parent.parent:
                parent = parent.parent
                level += 1
                if level > 3:
                    raise serializers.ValidationError("Maksimal 3 darajali izohga ruxsat berilgan.")
        return data
