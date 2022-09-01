from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CustomUser
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validate_data):
        return CustomUser.objects.create(**validate_data)