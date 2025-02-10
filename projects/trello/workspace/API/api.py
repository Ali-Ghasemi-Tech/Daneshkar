from rest_framework import serializers , status , permissions
from .serializer import WorkspaceCreateSerializer , BoardSerializer , TaskSerializer , WorkspaceUpdateDeleteSerializer , BoardUpdateDeleteSerializer , TaskStatusUpdate
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , UpdateAPIView , RetrieveUpdateAPIView
from ..models import Workspace , Board , Task
from django.shortcuts import get_object_or_404
from .permissions import IsOwner  , IsWorkspaceOwner , IsOwnerOrMember , IsOwnerOrMemberBoard , CanUpdateStatus
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

class BoardCreateApiView(ListCreateAPIView):
   
    serializer_class = BoardSerializer

    def get_permissions(self):
        if self.request.method  == 'POST':
            return [IsWorkspaceOwner()] 
        return [IsOwnerOrMember()]

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
    
    def perform_create(self, serializer):
        workspace_id = self.kwargs.get('workspace_id')
        self.workspace = get_object_or_404(Workspace, pk=workspace_id)
        serializer.save(workspace = self.workspace)
  
class BoardUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = BoardUpdateDeleteSerializer
    lookup_url_kwarg = 'board_id'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsWorkspaceOwner()]
        return [IsOwnerOrMember()]

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

class TaskCreateApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'board_id'

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsWorkspaceOwner()]
        return [CanUpdateStatus()]

    def get_queryset(self):
        board_id = self.kwargs.get('board_id')
        self.board = get_object_or_404(Board, pk=board_id)
        return Task.objects.filter(board=self.board)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        board_id = self.kwargs.get('board_id')
        self.board = get_object_or_404(Board, pk=board_id)

        # ***KEY CHANGE: Resolve the Many-to-Many relationship***
        users = self.board.users.all()  # Get the actual Member instances

        context['users'] = users
        context['board'] = self.board
        return context
    
    def perform_create(self, serializer):
        board_id = self.kwargs.get('board_id')
        self.board = get_object_or_404(Board, pk=board_id)
        serializer.save(board = self.board)
    
class TaskUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'

    def get_permissions(self):
        if self.request.method == 'GET':
            return[CanUpdateStatus()]
        return [IsWorkspaceOwner()]

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        return Task.objects.filter(id =task_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        board_id = self.kwargs.get('board_id')
        self.board = get_object_or_404(Board, pk=board_id)

        # ***KEY CHANGE: Resolve the Many-to-Many relationship***
        users = self.board.users.all()  # Get the actual Member instances

        context['users'] = users  # Pass the resolved members to the context
        return context
    
class TaskStatusUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = TaskStatusUpdate
    permission_classes = [CanUpdateStatus]
    lookup_url_kwarg = 'task_id'

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        return Task.objects.filter(id =task_id)