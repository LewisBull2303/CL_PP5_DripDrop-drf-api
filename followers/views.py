# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from models import Followers
from dripdrop.permissions import IsOwnerOrReadOnly
from .serializers import FollowerSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class FollowersList(generics.ListCreateAPIView):
    """
    The class for my followers list
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowersDetail(generics.RetrieveDestroyAPIView):
    """
    The class for the Followers Details
    Allows users to see a follower or
    unfollow another user
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Followers.objects.all()