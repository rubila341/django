from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubTaskViewSet, CategoryViewSet, TaskStatsView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubTaskViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'task-stats', TaskStatsView, basename='task-stats')

urlpatterns = [
    path('', include(router.urls)),
]
