# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer

class SetListAPI(APIView):
    # add permission to check if user is authenticated

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        return Response("Response data song list")