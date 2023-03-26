from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Video


# @require_http_methods(['GET'])
# def get_videos(request):
#     videos = Video.objects.order_by('publish_datetime')
#     paginator = Paginator(videos, 10)  # Show 10 videos per page
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     data = {
#         'count': paginator.count,
#         'num_pages': paginator.num_pages,
#         'has_next': page_obj.has_next(),
#         'has_previous': page_obj.has_previous(),
#         'results': [
#             {
#                 'title': video.title,
#                 'description': video.description,
#                 'url': video.url,
#                 'publish_datetime': video.publish_datetime,
#             }
#             for video in page_obj
#         ]
#     }
#
#     return JsonResponse(data)
#
#
# @require_http_methods(['GET'])
# def search_videos(request):
#     query = request.GET.get('q')
#     if not query:
#         return JsonResponse({'error': 'Query parameter "q" is required.'}, status=400)
#
#     videos = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
#
#     data = {
#         'count': videos.count(),
#         'results': [
#             {
#                 'title': video.title,
#                 'description': video.description,
#                 'url': video.url,
#                 'publish_datetime': video.publish_datetime,
#             }
#             for video in videos
#         ]
#     }
#
#     return JsonResponse(data)

@require_http_methods(['GET'])
def get_videos(request):
    videos = Video.objects.order_by('-publish_datetime')
    paginator = Paginator(videos, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    query = request.GET.get('q')
    if query:
        page_obj = videos.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'youtube_app/video_list.html', context)


@require_http_methods(['GET'])
def search_videos(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'youtube_app/video_list.html', {'error': 'Query parameter "q" is required.'})
    videos = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-publish_datetime')
    paginator = Paginator(videos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'youtube_app/video_list.html', context)
