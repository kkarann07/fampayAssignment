from celery import Celery
from django.conf import settings
from googleapiclient.discovery import build

from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from .models import Video

app = Celery('tasks', broker=settings.CELERY_BROKER_URL)

API_KEYS = ['AIzaSyCK8LYpjbIp1h2-030VtpJbwUr-rczPI8U', 'API_KEY_2', 'API_KEY_3']

API_KEY_INDEX = 0


@app.task
def fetch_latest_videos():
    global API_KEY_INDEX

    # youtube = get_youtube_service(API_KEYS[API_KEY_INDEX])
    youtube = build('youtube', 'v3', developerKey=API_KEYS[API_KEY_INDEX])

    try:
        # search for videos uploaded in the last 60 seconds
        now = datetime.utcnow()
        published_after = (now - timedelta(seconds=60)).isoformat() + 'Z'
        search_response = youtube.search().list(
            part='id,snippet',
            q='money',
            type='video',
            publishedAfter=published_after
        ).execute()

        videos = []

        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_response = youtube.videos().list(
                part='snippet',
                id=video_id
            ).execute()
            video = video_response['items'][0]
            videos.append(Video(
                youtube_id=video['id'],
                title=video['snippet']['title'],
                description=video['snippet']['description'],
                thumbnail_url=video['snippet']['thumbnails']['default']['url'],
                publish_datetime=video['snippet']['publishedAt'],
                url=f'https://www.youtube.com/watch?v={video["id"]}'
            ))

        Video.objects.bulk_create(videos)
        return str(videos)

    except HttpError as e:
        # switch to the next API key if the current key's quota is exhausted
        if e.resp.status == 403 and 'quotaExceeded' in e.content.decode():
            API_KEY_INDEX = (API_KEY_INDEX + 1) % len(API_KEYS)
            fetch_latest_videos.delay()
        else:
            # log the error
            print('An error occurred: %s' % e)
    except Exception as e:
        # log the error
        print('An error occurred: %s' % e)
