from rest_framework import serializers
from django.http import Http404, HttpResponseBadRequest
from .models import CustomUser
from scholarships.models import Scholarships
from django.contrib.auth.hashers import make_password



class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    gender = serializers.CharField(max_length=2, required=False)
    indigenous_status = serializers.CharField(max_length=2, required=False)
    vision_impairment = serializers.CharField(max_length=2, required=False)
    low_income = serializers.CharField(max_length=2, required=False)
    esol = serializers.CharField(max_length=2, required=False)
    duration = serializers.CharField(max_length=2, required=False)
    education = serializers.CharField(max_length=2, required=False)
    employment = serializers.CharField(max_length=2, required=False)
    industry = serializers.CharField(max_length=2, required=False)
    post_code = serializers.IntegerField(required=False)
    year_of_birth = serializers.IntegerField(required=False)
    favorites = serializers.SlugRelatedField(many=True, slug_field='scholarship', queryset=Scholarships.objects.all())

    def create(self, validate_data):
        try: 
            validate_data['password'] = make_password(validate_data['password'])
            return CustomUser.objects.create(**validate_data)
        except KeyError:
            raise HttpResponseBadRequest

    def update(self, instance, validate_data):
        instance.username = validate_data.get('username', instance.username)
        instance.email = validate_data.get('email', instance.email)
        instance.post_code = validate_data.get('post_code', instance.post_code)
        instance.year_of_birth = validate_data.get('year_of_birth', instance.year_of_birth)
        instance.gender = validate_data.get('gender', instance.gender)
        instance.indigenous_status = validate_data.get('indigenous_status', instance.indigenous_status)
        instance.vision_impairment = validate_data.get('vision_impairment', instance.vision_impairment)
        instance.low_income = validate_data.get('low_income',instance.low_income)
        instance.esol = validate_data.get('esol',instance.esol)
        instance.education = validate_data.get('education',instance.education)
        instance.employment = validate_data.get('employment',instance.employment)
        instance.industry = validate_data.get('industry',instance.industry)
        if "password" in validate_data.keys():
            instance.password = make_password(validate_data.get('password'))
        instance.save()
        return instance

