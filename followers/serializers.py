# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import IntegrityError
from rest_framework import serializers

# Internal:
from .models import Followers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class FollowerSerializer(serializers.ModelSerializer):
    """
    Class for the Follower Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_user = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Followers
        fields = [
            'id',
            'owner',
            'followed',
            'created_on',
            'followed_user'
        ]
    
    def create(self, validated_data):
        """
        Handle possible duplication
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplication Found'
            })