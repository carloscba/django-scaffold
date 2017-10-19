from rest_framework import serializers
from . import models

class AltarcitosSerializer(serializers.ModelSerializer):
    """A serializer for user profile objects"""
    #name = serializers.CharField(max_length=10)

    class Meta:
        model = models.Altarcitos
        fields = ('id','name', 'username', 'message', 'photo', 'uid')   