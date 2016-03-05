from django.conf.urls import include, url

urlpattern = [
    url(r'videos', include())
]

"""
/api/videos/
/api/playlists/
/api/screens/
/api/tags/
/api/
"""