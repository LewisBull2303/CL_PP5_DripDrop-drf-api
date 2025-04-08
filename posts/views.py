# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Post
from .serializers import PostSerializer
from dripdrop.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PostList(generics.ListCreateAPIView):
    """
    A class view for the PostList
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_number=Count(
            'comment',
            distinct=True
        ),
        likes_number=Count(
            'likes',
            distinct=True
        )
    ).order_by('-created_on')