from rest_framework import serializers
from django.http import Http404, HttpResponseBadRequest
from .models import CustomUser
from django.contrib.auth.hashers import make_password
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validate_data):
        try: 
            validate_data['password'] = make_password(validate_data['password'])
            return CustomUser.objects.create(**validate_data)
        except KeyError:
            raise HttpResponseBadRequest

    def update(self, instance, validate_data):
        instance.username = validate_data.get('username', instance.username)
        instance.email = validate_data.get('email', instance.email)
        if "password" in validate_data.keys():
            instance.password = make_password(validate_data.get('password'))
        instance.save()
        return instance

        