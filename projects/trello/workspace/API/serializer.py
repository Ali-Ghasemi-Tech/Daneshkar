from ..models import Workspace , Board , Task , MemberModel
from rest_framework import serializers , status , permissions
from django.shortcuts import get_object_or_404


class WorkspaceCreateSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()  
    member_ids = serializers.PrimaryKeyRelatedField(
        queryset=MemberModel.objects.all(),
        source='members',
        write_only=True,
        many=True
    )
   
    class Meta:
        model = Workspace
        exclude = ['is_active']
        read_only_fields = ['owner']

    def get_members(self, obj):
        return [user.username for user in obj.members.all()]

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        workspace = Workspace.objects.create(**validated_data)
        workspace.members.set(members)
        return workspace

class WorkspaceUpdateDeleteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Workspace
        fields = ['owner', 'name' , 'members', 'is_active', 'private']
        
class BoardSerializer(serializers.ModelSerializer):
    query = MemberModel.objects.none()
   
    def __init__(self, *args, **kwargs):
        workspace_members = kwargs.get('context').get('members')  # Correct key: workspace_members
        # print(kwargs.get('context').get('users'))
        super().__init__(*args, **kwargs)
        if workspace_members:
            print(workspace_members)
            self.query = workspace_members  # Correct key: workspace_members
            
        self.fields['users'] = serializers.PrimaryKeyRelatedField(queryset=self.query, many=True)
    

    class Meta:
        model = Board
        exclude = ['start' , 'done' , 'is_active']
        read_only_fields = ['workspace']

class BoardUpdateDeleteSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        workspace_members = kwargs.get('context').get('members')  # Correct key: workspace_members
        workspace = kwargs.get('context').get('workspace')
        # print(kwargs.get('context').get('users'))
        super().__init__(*args, **kwargs)
        if workspace_members:
            print(workspace_members)
            self.query = workspace_members  # Correct key: workspace_members
            
        self.fields['users'] = serializers.PrimaryKeyRelatedField(queryset=self.query, many=True)
        
            
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['start' , 'workspace']

class TaskSerializer(serializers.ModelSerializer):
    query = MemberModel.objects.none()
   
    def __init__(self, *args, **kwargs):
        board_users = kwargs.get('context').get('users') 
        super().__init__(*args, **kwargs)

        if board_users:
            self.query = board_users  
        self.fields['assigned_to'] = serializers.PrimaryKeyRelatedField(queryset = self.query, many = False)

        
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['board' , 'start_time']

    def create(self , validated_data):
        if validated_data['title'] in Task.objects.filter(board = validated_data['board']).values_list('title' , flat= True):
            raise serializers.ValidationError("task already exists.")
        else:
            return super().create(validated_data)
        # print((validated_data['title'] , ) in Task.objects.filter(board = validated_data['board']).values_list('title'))
        # return super().create(validated_data)

class TaskStatusUpdate(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['title' , 'assigned_to' , 'description' , 'start_time' , 'deadline' , 'board']