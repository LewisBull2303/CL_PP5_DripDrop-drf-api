# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Profile
from .serializers import ProfileSerializer
from dripdrop.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileList(generics.ListAPIView):
    """
    A class view for the ProfileList
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_number=Count(
            'owner__post',
            distinct=True
        ),
        followers_number=Count(
            'owner__followed',
            distinct=True
            ),
        following_number=Count(
            'owner__following',
            distinct=True
        )
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'posts_number',
        'followers_number',
        'following_number',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]
    search_fields = [
        'owner__username',
    ]
    filterset_fields = [
        # filter profiles that are following a specific profile
        'owner__following__followed__profile',
        # get profiles that are followed by a specific profile
        'owner__followed__owner__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the Profile Detail
    """
    serializer_class = ProfileSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Profile.objects.annotate(
        posts_number=Count(
            'owner__post',
            distinct=True
        ),
        followers_number=Count(
            'owner__followed',
            distinct=True
            ),
        following_number=Count(
            'owner__following',
            distinct=True
        )
    ).order_by('-created_on')

    def delete(self, request, pk):
        """
        Delete a profile by id
        """
        user = self.request.user
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )