# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    SetListAPI,
)
from rest_framework import routers



urlpatterns = [
    path('api', SetListAPI.as_view()),
]