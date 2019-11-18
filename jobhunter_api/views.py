from jobhunter_api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from jobhunter_api import serializers
from jobhunter_api import models
from jobhunter_api import permissions
# from profile_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class OpeningsViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and openings"""
    serializer_class = serializers.OpeningsSerializer
    queryset = models.Openings.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description',)


