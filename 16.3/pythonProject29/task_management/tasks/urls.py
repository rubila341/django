from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskListCreateView, TaskDetailView, SubTaskListCreateView, SubTaskDetailView

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
]
