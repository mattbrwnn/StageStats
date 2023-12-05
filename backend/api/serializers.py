from os import name
from rest_framework import serializers
from .models import Album, Artist, Song
# Each serializer serves to format the data to be stored into the database
class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.SlugRelatedField(
        slug_field='artist_name', 
        queryset=Artist.objects.all()
    )
    album_name = serializers.SlugRelatedField(
        slug_field='album_name', 
        queryset=Album.objects.all()
    )

    class Meta:
        model = Song
        fields = ['title', 'artist_name', 'album_name', 'play_count']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    artist_name = serializers.SlugRelatedField(
        slug_field='artist_name', 
        queryset=Artist.objects.all()
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist_name', 'songs', 'year']

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'albums']