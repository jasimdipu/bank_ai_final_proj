from django.urls import path
from . import views

urlpatterns = [
    path('data', views.CustomerListView.as_view(), name='customers_data'),
    path('upload-csv/', views.UploadCSVView.as_view(), name='upload-csv'),
    path('train-model/', views.TrainModelView.as_view(), name='train-model'),
]
