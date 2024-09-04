from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('', hello_view),
]
