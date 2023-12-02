from rest_framework import serializers
from .models import *
class students_data_serializer(serializers.ModelSerializer):
    class Meta:
        model=students_data
        fields="__all__"