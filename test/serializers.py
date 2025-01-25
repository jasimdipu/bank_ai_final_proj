from rest_framework import serializers
from .models import TestModel, TestModel2


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['id', 'name']


class TestModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel2
        fields = ['id', 'name', 'description']
