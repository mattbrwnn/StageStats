# todo/todo_api/views.py
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Album, Song
from .algorithms import QuickSort, MergeSort
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from .setlistscraper import getSongsPlayed
from django.http import JsonResponse

#Defines the API's behavior when receiving GET and POST requests, specifically used to retrieve artist song data
class SetListAPI(APIView):
    def get(self, request, format=None):
        artist_name = request.query_params.get('artist', '')
        if artist_name:
            try:
                song_counts_response = JsonResponse(getSongsPlayed(artist_name))
                
                return song_counts_response
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Artist name is required"}, status=status.HTTP_400_BAD_REQUEST)
       

    def post(self, request):
        if 'artist_name' in request.data:
            serializer = ArtistSerializer(data=request.data)

        elif 'album_name' in request.data:
            serializer = AlbumSerializer(data=request.data)

        elif 'title' in request.data:
            serializer = SongSerializer(data=request.data)

        else:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Handles sorting requests from the frontend

class QuickSortAPI(APIView):
    def post(self, request):
        data = request.data.get('list', [])
        QuickSort(data, 0, len(data) - 1)
        return Response(data, status=status.HTTP_201_CREATED)

class MergeSortAPI(APIView):
    def post(self, request):
        data = request.data.get('list', [])
        MergeSort(data, 0, len(data) - 1)
        return Response(data, status=status.HTTP_201_CREATED)