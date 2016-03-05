from django.contrib.auth.models import User
from django.db import models

MEDIA_TYPES = {
	'img': 'Splash',
	'vid': 'Video'
}


class PlayDatetime(models.Model):
    """
    Abstract model for datetime
    """
    created_ts = models.DateTimeField(auto_now_add=True, help_text="Created timespan")
    updated_ts = models.DateTimeField(auto_now_add=False, auto_now=True, help_text="Updated timestamp")

    class Meta:
        abstract = True

class Tag(PlayDatetime):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name


class Video(PlayDatetime):
    """
    Video data
    """
    created_by = models.ForeignKey(User)
    url = models.CharField(max_length=255, help_text="Video Url")
    title = models.CharField(max_length=100)
	descritpion = models.TextField(blank=True, null=True)
	tag = models.ManyToManyKey(Tag)

    def __unicode__(self):
        return self.title

class Spash(PlayDatetime):
    """
    Image data
    """
    created_by = models.ForeignKey(User)
    url = models.CharField(max_length=255, help_text="Video Url")
    title = models.CharField(max_length=100)
	descritpion = models.TextField(blank=True, null=True)
	tag = models.ManyToManyField(Tag)
	timeout = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.title


class Playlist(PlayDatetime):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey(User)

	def __unicode__(self):
		return self.name


class Screen(PlayDatetime):
	title = models.CharField(max_length=100)
	playlist = models.ForeignKey(Playlist)
	type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='vid')
	video = models.ForeignKey(Video, blank=True, null=True)
	spalsh = models.ForeignKey(Splash, blank=True, null=True)
	order = models.PositiveSmallIntegerField()
	is_active = models.BooleanField(default=True, help_text="Flags to mark data as active or inactive")	
	
	def __unicode__(self):
		return self.title
