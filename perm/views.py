from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets

from perm.models import Song
from perm.serializers import SongModelSerializer


class TrialPerm(permissions.DjangoObjectPermissions):
    authenticated_users_only = False
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
    permission_classes = [TrialPerm]