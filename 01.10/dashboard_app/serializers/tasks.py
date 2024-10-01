from rest_framework import serializers
from dashboard_app.models import Task

class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'priority']
