# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PostSerializer(serializers.ModelSerializer):
    """
    A class for a PostSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_number = serializers.ReadOnlyField()
    likes_number = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validation of the uploaded image size
        """
        # Image height limit of 4096 px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Your image exceeds the height limit of 4096px.'
            )