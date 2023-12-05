# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    SetListAPI, QuickSortAPI, MergeSortAPI,
)

from rest_framework import routers



urlpatterns = [
    path('api', SetListAPI.as_view()),
     path('merge-sort', MergeSortAPI.as_view(), name='merge-sort'),
    path('quick-sort', QuickSortAPI.as_view(), name='quick-sort'),
]