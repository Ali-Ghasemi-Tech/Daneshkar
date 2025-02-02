from django.urls import path 
from .API.api import WorkspaceCreateApiView , BoardApiView , TaskApiView , WorkspaceUpdateDeleteView

urlpatterns = [
    path('' , WorkspaceCreateApiView.as_view() , name='workspace'),
    path('<int:workspace_id>/update/' , WorkspaceUpdateDeleteView.as_view() , name='workspace_update'),
    path('<int:workspace_id>/board' , BoardApiView.as_view() , name= 'board'),
    path('task' , TaskApiView.as_view() , name = 'task'),
]