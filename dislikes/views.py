from rest_framework import generics, permissions
from bjj_api.permissions import IsOwnerOrReadOnly
from dislikes.models import PostDislike, EventDislike
from .serializers import PostDislikeSerializer, EventDislikeSerializer

class PostDislikeList(generics.ListCreateAPIView):
    """
    List post dislikes or create a post dislike if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostDislikeSerializer
    queryset = PostDislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDislikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a post dislike or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostDislikeSerializer
    queryset = PostDislike.objects.all()

class EventDislikeList(generics.ListCreateAPIView):
    """
    List event dislikes or create an event dislike if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventDislikeSerializer
    queryset = EventDislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDislikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an event dislike or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventDislikeSerializer
    queryset = EventDislike.objects.all()
