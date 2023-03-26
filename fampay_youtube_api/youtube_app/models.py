from django.db import models


class Video(models.Model):
    """
    Model for storing YouTube video information.
    """
    youtube_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    thumbnail_url = models.URLField(max_length=1000)
    publish_datetime = models.DateTimeField()
    url = models.URLField(max_length=1000)
