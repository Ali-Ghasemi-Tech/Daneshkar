from django.urls import path 
from .API.api import WorkspaceCreateApiView , BoardCreateApiView , TaskCreateApiView , WorkspaceUpdateDeleteView , BoardUpdateDeleteApiView , TaskUpdateDeleteApiView , TaskStatusUpdateApiView
 
urlpatterns = [
    path('' , WorkspaceCreateApiView.as_view() , name='workspace'),
    path('<int:workspace_id>/update/' , WorkspaceUpdateDeleteView.as_view() , name='update_workspace'),
    path('<int:workspace_id>/board/' , BoardCreateApiView.as_view() , name= 'board'),
    path('<int:workspace_id>/board/<int:board_id>/update' , BoardUpdateDeleteApiView.as_view() , name='update_board'),
    path('<int:workspace_id>/board/<int:board_id>/task' , TaskCreateApiView.as_view() , name = 'task'),
    path('<int:workspace_id>/board/<int:board_id>/task/<int:task_id>/update' , TaskUpdateDeleteApiView.as_view() , name='update_task'),
    path('<int:workspace_id>/board/<int:board_id>/task/<int:task_id>/update_status' , TaskStatusUpdateApiView.as_view() , name='update_task_status'),

]