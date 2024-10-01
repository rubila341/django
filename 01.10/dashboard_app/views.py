from django.shortcuts import get_object_or_404
from dashboard_app.serializers.projects import ProjectSerializer
from dashboard_app.serializers.tasks import AllTasksSerializer
from dashboard_app.serializers.tags import TagSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from dashboard_app.models import Project, Task, Tag

@api_view(['GET'])
def get_projects(request: Request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def task_list(request, project_name=None):
    if project_name:
        project = get_object_or_404(Project, name=project_name)
        tasks = Task.objects.filter(project=project)
    else:
        tasks = Task.objects.all()

    serializer = AllTasksSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_tags(request: Request):
    """
    Функция для получения всех тегов в формате JSON.
    """
    tags = Tag.objects.all()  # Получаем все теги
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
def get_tag(request: Request, tag_id: int):
    """
    Функция для получения и обновления информации о теге по его ID.
    """
    tag = get_object_or_404(Tag, id=tag_id)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

