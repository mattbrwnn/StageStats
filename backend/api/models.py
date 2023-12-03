# todo/todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)


class Album(models.Model):
    album_name = models.CharField(max_length=100, default="NULL_ALBUM")
    artist_name = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    year = models.IntegerField(default=1)


class Song(models.Model):
    title = models.CharField(max_length=100, default='NULL_SONG')
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    play_count = models.IntegerField(default=1)