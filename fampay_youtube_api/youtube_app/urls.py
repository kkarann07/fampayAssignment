from django.urls import path

from .views import get_videos, search_videos

urlpatterns = [
    path('videos/', get_videos, name='get_videos'),
    path('videos/search/', search_videos, name='search_videos')
]
