from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = Author
        fields = ['id', 'name', 'email']
