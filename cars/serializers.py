from rest_framework import serializers
from cars.models import Car

class CarSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['year', 'make', 'gas_milage', ] 