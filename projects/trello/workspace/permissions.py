from rest_framework.permissions import BasePermission
from .models import Workspace , Board , Task


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
    
class IsMemberOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)    
    
class IsWorkspaceOwner(BasePermission):
     def has_permission(self, request, view):
        workspace_id = request.data.get('workspace') or view.kwargs.get('workspace_id')
        workspace = Workspace.objects.get(id=workspace_id)
        return request.user == workspace.owner
    
class IsOwnerOrMember(BasePermission):
  def has_permission(self, request, view):
        workspace_id = request.data.get('workspace') or view.kwargs.get('workspace_id')
        workspace = Workspace.objects.get(id=workspace_id)
        return request.user == workspace.owner or request.user in workspace.members.all()
  
class IsOwnerOrMemberBoard(BasePermission):
    def has_permission(self, request, view):
        workspace_id = request.data.get('workspace') or view.kwargs.get('workspace_id')
        board_id = request.data.get('board') or view.kwargs.get('board_id')
        board =Board.objects.get(id = board_id)
        workspace = Workspace.objects.get(id=workspace_id)
        return request.user == workspace.owner or request.user in board.users.all()
    
class CanUpdateStatus(BasePermission):
    def has_permission(self, request, view):
        workspace_id = request.data.get('workspace') or view.kwargs.get('workspace_id')
        workspace = Workspace.objects.get(id=workspace_id)
        task_id = request.data.get('task') or view.kwargs.get('task_id')
        if task_id:
            task = Task.objects.get(id= task_id)
            return request.user == task.assigned_to
        return request.user == workspace.owner