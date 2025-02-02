from rest_framework import serializers , status , permissions
from .serializer import WorkspaceCreateSerializer , BoardSerializer , TaskSerializer , WorkspaceUpdateDeleteSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from ..models import Workspace , Board , Task
from django.shortcuts import get_object_or_404
from .permissions import IsOwner

class WorkspaceCreateApiView(ListCreateAPIView):
    serializer_class = WorkspaceCreateSerializer

    def get_queryset(self):
        Workspace.objects.filter(owner = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class WorkspaceUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkspaceUpdateDeleteSerializer
    permission_classes = [IsOwner]
    lookup_url_kwarg = 'workspace_id'

    def get_queryset(self):
        workspace_id = self.kwargs.get('workspace_id')
        print(workspace_id)
        return Workspace.objects.filter(id = workspace_id)

class BoardApiView(ListCreateAPIView):
   
    serializer_class = BoardSerializer

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
        return context

class TaskApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer