from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Video(models.Model):
    """ Video data """
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='videos')

    def __unicode__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Screen(models.Model):
    MEDIA_TYPES = (
        ('image', 'Splash'),
        ('video', 'Video')
    )

    title = models.CharField(max_length=255)
    playlist = models.ForeignKey(Playlist)
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    video = models.ForeignKey(Video, blank=True, null=True)
    order = models.IntegerField()
    description = models.TextField()    # if this is a
    timeout = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title
