
from rest_framework import serializers
from .models import CustomUser
from django.http import Http404, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        try:
            validated_data['password'] = make_password(validated_data['password'])
            return CustomUser.objects.create(**validated_data)
        except KeyError:
            raise HttpResponseBadRequest

    def create(self, validate_data):
        return CustomUser.objects.create(**validate_data)