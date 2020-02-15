from django.db import models
from django.contrib.auth.models import User

# user create
# User.objects.create_user('gghotted', 'elwlahs2')

# ManyToMany model create
# music = Music()
# music.save()
# playList = PlayList(user=user)
# playList.save()
# playList.add(music)
# playList.musics.create(url='test')

# ManyToMany model get queryset
# music.playlists.all()
# playList.musics.all()


class Music(models.Model):
    url = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PlayList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    musics = models.ManyToManyField(Music, related_name="playlists")
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



