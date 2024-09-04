import django_filters
from .models import Task, SubTask

class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    deadline = django_filters.DateFilter(field_name='deadline', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['status', 'deadline']

class SubTaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    deadline = django_filters.DateFilter(field_name='deadline', lookup_expr='lte')

    class Meta:
        model = SubTask
        fields = ['status', 'deadline']
