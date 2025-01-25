from django.urls import path
from .views import TestModelList, TestModel2List, UpdateTestModelList


urlpatterns = [
    path('test', TestModelList.as_view(), name='test-model-list'),
    path('test-update/<str:pk>', UpdateTestModelList.as_view(), name='test-model-update'),
    path('test2', TestModel2List.as_view(), name='test-model2-list'),
]

