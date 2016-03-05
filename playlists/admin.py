from django.contrib import admin

from playlists.models import Tag, Video, Playlist, Screen

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(Playlist)
admin.site.register(Screen)
