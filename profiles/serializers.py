# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProfileSerializer(serializers.ModelSerializer):
    """
    A class for a Profile Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_number = serializers.ReadOnlyField()
    followers_number = serializers.ReadOnlyField()
    following_number = serializers.ReadOnlyField()

    def check_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner
