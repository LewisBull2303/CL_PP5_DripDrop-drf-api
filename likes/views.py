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