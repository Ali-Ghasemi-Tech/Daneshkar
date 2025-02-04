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
        exclude = ['start' , 'done' , 'workspace']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = 'start_time'