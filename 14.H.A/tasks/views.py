from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Count
from .models import Task, SubTask, Category
from .serializers import (
    TaskCreateSerializer, TaskDetailSerializer,
    SubTaskCreateSerializer, SubTaskSerializer,
    CategoryCreateSerializer, CategorySerializer
)
from .filters import TaskFilter, SubTaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        count = category.task_set.count()
        return Response({'task_count': count})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['created_at']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateSerializer
        return TaskDetailSerializer

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = SubTaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['created_at']

class TaskStatsView(viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        now = timezone.now()
        total_tasks = Task.objects.count()
        tasks_by_status = Task.objects.values('status').annotate(count=Count('id'))
        overdue_tasks = Task.objects.filter(deadline__lt=now).count()

        return Response({
            'total_tasks': total_tasks,
            'tasks_by_status': list(tasks_by_status),
            'overdue_tasks': overdue_tasks
        })
