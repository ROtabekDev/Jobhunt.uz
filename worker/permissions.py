from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import Worker

class IsWorkerUser(permissions.BasePermission):
    def has_permission(self, request, view):

        if Worker.objects.filter(user=request.user).exists():
            return True
        raise PermissionDenied('Afsus :(. Worker bo`lishingiz kerak.')