from rest_framework import permissions


class IsSuperUserOrSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
    
class IsSuperUserOrNotAuthenticated(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_superuser or not request.user.is_authenticated

    
class IsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj
