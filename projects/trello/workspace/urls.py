from django.urls import path 
from .API.api import WorkspaceCreateApiView , BoardApiView , TaskApiView , WorkspaceUpdateDeleteView , BoardUpdateDeleteApiView

urlpatterns = [
    path('' , WorkspaceCreateApiView.as_view() , name='workspace'),
    path('<int:workspace_id>/update/' , WorkspaceUpdateDeleteView.as_view() , name='update_workspace'),
    path('<int:workspace_id>/board/' , BoardApiView.as_view() , name= 'board'),
    path('<int:workspace_id>/board/<int:board_id>/update' , BoardUpdateDeleteApiView.as_view() , name='update_board'),
    path('task' , TaskApiView.as_view() , name = 'task'),
]