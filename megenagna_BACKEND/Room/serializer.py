from rest_framework import serializers
from .models import RoomProfile

class RoomProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomProfile
        fields = "__all__"
