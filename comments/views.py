from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from bjj_api.permissions import IsOwnerOrReadOnly
from .models import Comment,EventComment
from .serializers import CommentSerializer, CommentDetailSerializer
from .serializers import EventCommentSerializer, EventCommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
# EventComment Views
class EventCommentList(generics.ListCreateAPIView):
    serializer_class = EventCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = EventComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventCommentDetailSerializer
    queryset = EventComment.objects.all()