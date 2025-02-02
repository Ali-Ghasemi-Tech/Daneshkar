from ..models import Workspace , Board , Task , MemberModel
from rest_framework import serializers , status , permissions
from django.shortcuts import get_object_or_404


class WorkspaceCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    # members = serializers.PrimaryKeyRelatedField(
    #     queryset=MemberModel.objects.all(),  # All available members
    #     many=True,  # Important for many-to-many
    #     widget=serializers.CheckboxSelectMultiple  # Use checkbox widget
    # )
    class Meta:
        model = Workspace
        exclude = ['is_active']
        read_only_fields = ['owner']


        # def create(self, validated_data,request):
        #         validated_data['owner'] = request.user.id
        #         return super().create(validated_data)
        
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