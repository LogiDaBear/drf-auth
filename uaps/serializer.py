from rest_framework import serializers
from .models import UAPS


class UAPSSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'velocity', 'seen_by', 'description', 'updated_at', 'created_at')
        model = UAPS