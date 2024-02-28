from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Status
        fields = ['id', 'user', 'username', 'content', 'created_at']