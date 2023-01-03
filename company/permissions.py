from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import Company

class IsCompanyUser(permissions.BasePermission):
    def has_permission(self, request, view):

        if Company.objects.filter(user=request.user).exists():
            return True
        raise PermissionDenied('Afsus :(. Kompaniya bo`lishingiz kerak.')