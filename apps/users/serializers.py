from rest_framework import serializers
from . import models

class UsersSerializer(serializers.ModelSerializer):
    """A serializer for user profile objects"""
    #name = serializers.CharField(max_length=10)

    class Meta:
        model = models.Users
        fields = ('id','displayName', 'email', 'photoURL', 'uid')   