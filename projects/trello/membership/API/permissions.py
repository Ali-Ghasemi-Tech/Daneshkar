from rest_framework import permissions


class IsSuperUserOrSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj

    
class IsSuper(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj
