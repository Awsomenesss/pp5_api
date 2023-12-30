from rest_framework import generics, permissions
from bjj_api.permissions import IsOwnerOrReadOnly
from likes.models import PostLike, EventLike
from .serializers import PostLikeSerializer, EventLikeSerializer

class PostLikeList(generics.ListCreateAPIView):
    """
    List post likes or create a post like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a post like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()

class EventLikeList(generics.ListCreateAPIView):
    """
    List event likes or create an event like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventLikeSerializer
    queryset = EventLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an event like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventLikeSerializer
    queryset = EventLike.objects.all()
