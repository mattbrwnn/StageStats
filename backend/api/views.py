# todo/todo_api/views.py
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
<<<<<<< Updated upstream
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class SetListAPI(APIView):
    def get(self, request, format=None, *args, **kwargs):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

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
=======
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from django.http import JsonResponse
from repertorio import Repertorio

api = Repertorio('4HgFs37ud5OQhHs48Go6mO6j6GFiqHpFaMof')

def get_artist_setlist(request, artist_name):
    if request.method == 'GET':
        try:
            setlists = api.setlists(artistName=artist_name)
            return JsonResponse(setlists, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class SetListAPI(APIView):
    def get(self, request, *args, **kwargs):
        
        return Response("Response data song list")
>>>>>>> Stashed changes
