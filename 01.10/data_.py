from django.utils import timezone
from django.contrib.auth.models import User
from dashboard_app.models import ProjectFile, Project, Tag, Task
from django.core.files import File
from django.conf import settings
import os
import random


def populate_database():
    # Создание пользователей
    users = []
    for i in range(10):
        user = User.objects.create_user(f'user{i}', f'user{i}@example.com', 'password')
        users.append(user)

    # Создание тегов
    tags = []
    for tag_name in ['Срочно', 'Важно', 'Баг', 'Фича', 'Документация']:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        tags.append(tag)

    # Создание проектов и файлов проектов
    for i in range(8):
        project = Project.objects.create(
            name=f'Проект {i}',
            description=f'Описание проекта {i}'
        )

        # Создание файлов проекта
        for j in range(2):
            file_path = os.path.join(settings.MEDIA_ROOT, 'temp_file.txt')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f'Содержимое файла для проекта {i}, файл {j}')

            with open(file_path, 'rb') as f:
                project_file = ProjectFile.objects.create(
                    name=f'Файл {j} проекта {i}',
                    file=File(f, name=f'project_{i}_file_{j}.txt')
                )

            project.file.add(project_file)

        # Создание задач для проекта
        for k in range(8):
            task = Task.objects.create(
                title=f'Задача {k} для проекта {i}',
                description=f'Описание задачи {k} для проекта {i}',
                status=random.choice(['New', 'In Progress', 'Done']),
                priority=random.choice(['Low', 'Medium', 'High']),
                project=project,
                due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                assignee=random.choice(users)
            )
            task.tags.set(random.sample(tags, random.randint(1, 3)))

    print("База данных успешно заполнена.")


if __name__ == '__main__':
    populate_database()