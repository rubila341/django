from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import User
from django.test import TestCase

class UserApiTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя для теста
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
            phone="123456789",
            position="Developer",
            project="Project X"
        )
        self.client = APIClient()

    def test_get_user_details(self):
        """Тест успешного получения информации о пользователе"""
        # Отправляем GET-запрос на эндпоинт с существующим ID
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.id}))

        # Проверяем, что статус ответа 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что ответ содержит нужные поля и значения
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')
        self.assertEqual(response.data['email'], 'testuser@example.com')
        self.assertEqual(response.data['phone'], '123456789')
        self.assertEqual(response.data['position'], 'Developer')
        self.assertEqual(response.data['project'], 'Project X')

    def test_get_user_details_not_found(self):
        """Тест на получение информации о несуществующем пользователе"""
        # Отправляем GET-запрос на эндпоинт с несуществующим ID
        response = self.client.get(reverse('user-detail', kwargs={'pk': 999}))

        # Проверяем, что статус ответа 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Проверяем, что в ответе содержится сообщение о том, что пользователь не найден
        self.assertEqual(response.data['detail'], 'User not found')
