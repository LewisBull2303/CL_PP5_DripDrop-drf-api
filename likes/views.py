# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Like
from .serializers import LikeSerializer
from dripdrop.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class LikeList(generics.ListCreateAPIView):
    """
    A class for the LikeList
    """
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        # owner is the user
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    A class for LikeDetail
    User is able to to retrieve and delete their liked
    posts
    """
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Like.objects.all()