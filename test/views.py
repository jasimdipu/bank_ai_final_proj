from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import TestModel, TestModel2  # *
from .serializers import TestModelSerializer, TestModel2Serializer


class TestModelList(ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class UpdateTestModelList(RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class TestModel2List(ListAPIView):
    queryset = TestModel2.objects.all()
    serializer_class = TestModel2Serializer
