from pyexpat import model
from rest_framework import serializers
from .models import Scholarships 

class ScholarshipSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    organisation = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    url = serializers.CharField(max_length=200)
    closing_date = serializers.DateTimeField()
    owner = serializers.ReadOnlyField()

    def create (self, validated_data):
        return Scholarships.objects.create(**validated_data)