# todo/todo_api/views.py
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from .fmapi import get_artist_setlist

class SetListAPI(APIView):
    def get(self, request, format=None, *args, **kwargs):
        get_artist_setlist(request=request, artist_name="Pearl Jam")
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