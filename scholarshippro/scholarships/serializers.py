from rest_framework import serializers
from .models import Scholarships 





class ScholarshipSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    organisation = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    eligibility = serializers.CharField(max_length=None)
    image = serializers.URLField()
    url = serializers.CharField(max_length=200)
    closing_date = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    gender = serializers.CharField(max_length=2, required=False)
    indigenous_status = serializers.CharField(max_length=2, required=False)
    vision_impairment = serializers.CharField(max_length=2, required=False)
    low_income = serializers.CharField(max_length=2, required=False)
    esol = serializers.CharField(max_length=2, required=False)
    duration = serializers.CharField(max_length=2, required=False)

    def create (self, validated_data):
        scholarship = Scholarships.objects.create(**validated_data)
        return scholarship


class ScholarshipDetailSerializer(ScholarshipSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.organisation = validated_data.get('organisation', instance.organisation)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.url = validated_data.get('url', instance.url)
        instance.closing_date = validated_data.get('closing_date', instance.closing_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.eligibility = validated_data.get('eligibility', instance.eligibility)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.indigenous_status = validated_data.get('indigenous_status', instance.indigenous_status)
        instance.vision_impairment = validated_data.get('vision_impairment', instance.vision_impairment)
        instance.low_income = validated_data.get('low_income',instance.low_income)
        instance.esol = validated_data.get('esol',instance.esol)
        instance.duration = validated_data.get('duration',instance.duration)
        instance.save()
        return instance





