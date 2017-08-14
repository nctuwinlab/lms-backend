from rest_framework import permissions


class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only owner can get and update profile
        return obj.user == request.user

    def has_permission(self, request, view):
        if request.method == 'POST':
            # Method POST is only for create new user
            # And only superuser can create regular user
            return request.user.is_superuser
        else:
            return True
