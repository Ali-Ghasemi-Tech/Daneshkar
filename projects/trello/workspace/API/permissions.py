from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
    
class IsMemberOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
    
class IsParentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.workspace.owner
    
class IsWorkspaceOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.board.workspace.owner