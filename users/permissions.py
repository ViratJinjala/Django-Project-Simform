from rest_framework import permissions

class IsAdminUserCustom(permissions.BasePermission):
    """
    Allows access only to users with is_admin=True.
    """

    def has_permission(self, request, view):
        return bool(request.user.is_admin)
