from rest_framework import serializers
from .models import CustomerData


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = '__all__'  # Include all fields
        # You can also specify specific fields, e.g., `fields = ['id', 'name', 'price']`
