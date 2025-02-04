from rest_framework import serializers , status , permissions
from .serializer import WorkspaceCreateSerializer , BoardSerializer , TaskSerializer , WorkspaceUpdateDeleteSerializer , BoardUpdateDeleteSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from ..models import Workspace , Board , Task
from django.shortcuts import get_object_or_404
from .permissions import IsOwner , IsParentOwner
from django.db.models import Q

class WorkspaceCreateApiView(ListCreateAPIView):
    serializer_class = WorkspaceCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Workspace.objects.filter(owner = self.request.user )
        user = self.request.user
        return Workspace.objects.filter(Q(owner=user) | Q(members=user)).distinct()
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class WorkspaceUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkspaceUpdateDeleteSerializer
    permission_classes = [IsOwner]
    lookup_url_kwarg = 'workspace_id'

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_id')
        return Workspace.objects.filter(id = workspace_id) 

class BoardApiView(ListCreateAPIView):
   
    serializer_class = BoardSerializer
    permission_classes = [IsParentOwner , permissions.IsAuthenticated]

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_id')
        self.workspace = get_object_or_404(Workspace, pk=workspace_id)
        return Board.objects.filter(workspace=self.workspace)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        workspace_id = self.kwargs.get('workspace_id')
        self.workspace = get_object_or_404(Workspace, pk=workspace_id)

        # ***KEY CHANGE: Resolve the Many-to-Many relationship***
        members = self.workspace.members.all()  # Get the actual Member instances

        context['members'] = members  # Pass the resolved members to the context
        context['workspace'] = self.workspace
        return context
    
class BoardUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = BoardUpdateDeleteSerializer
    permission_classes = [IsParentOwner]
    lookup_url_kwarg = 'board_id'

    def get_queryset(self):
        board_id = self.kwargs.get('board_id')
        return Board.objects.filter(id = board_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        workspace_id = self.kwargs.get('workspace_id')
        self.workspace = get_object_or_404(Workspace, pk=workspace_id)

        # ***KEY CHANGE: Resolve the Many-to-Many relationship***
        members = self.workspace.members.all()  # Get the actual Member instances

        context['members'] = members  # Pass the resolved members to the context
        return context

class TaskApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer