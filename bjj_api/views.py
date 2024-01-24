from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from event.models import Event
from posts.serializers import PostSerializer
from event.serializers import EventSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count

from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({"message": "Welcome to my django rest framework API!"})


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
@api_view(['GET'])   
def combined_posts_events(request):
    search_query = request.query_params.get('search', '')
    owner_query = request.query_params.get('owner', '')

    posts = Post.objects.filter(title__icontains=search_query)
    events = Event.objects.filter(description__icontains=search_query)

    if owner_query:
        posts = posts.filter(owner__username=owner_query)
        events = events.filter(owner__username=owner_query)

    posts = posts.annotate(
        likes_count=Count('post_likes', distinct=True), 
        dislikes_count=Count('post_dislikes', distinct=True), 
        comments_count=Count('comment', distinct=True)
    )

    events = events.annotate(
        likes_count=Count('event_likes', distinct=True),
        dislikes_count=Count('event_dislikes', distinct=True), 
        comments_count=Count('eventcomment', distinct=True)
    )

    combined_list = sorted(
        list(posts) + list(events), 
        key=lambda instance: instance.created_at, 
        reverse=True
    )

    paginator = PageNumberPagination()
    paginated_list = paginator.paginate_queryset(combined_list, request)

    serialized_list = []
    for item in paginated_list:
        if isinstance(item, Post):
            serializer = PostSerializer(item, context={'request': request})
            serialized_list.append(serializer.data)
        elif isinstance(item, Event):
            serializer = EventSerializer(item, context={'request': request})
            serialized_list.append(serializer.data)

    return paginator.get_paginated_response(serialized_list)