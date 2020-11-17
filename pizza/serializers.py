from rest_framework import serializers
from . import models
class pizza_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.pizza_model
        fields=('__all__')#['pizza_type','pizza_size','toppings']
