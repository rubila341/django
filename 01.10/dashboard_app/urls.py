from django.urls import path
from dashboard_app.views import get_projects, task_list, get_tags, get_tag

urlpatterns = [
    path('api/projects/', get_projects, name='project-list'),
    path('api/tasks/', task_list, name='task-list'),
    path('api/tags/', get_tags, name='tag-list'),
    path('api/tags/<int:tag_id>/', get_tag, name='tag-detail'),
]
