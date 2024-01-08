from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from bjj_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer  

class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in.
    The perform_create method associates the event with the logged-in user.
    """
    serializer_class = EventSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        likes_count=Count('event_likes', distinct=True), 
       
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'event_likes__owner__profile', 
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'description',
    ]
    ordering_fields = [
        'likes_count',
        'event_likes__created_at', 
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer 
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        likes_count=Count('event_likes', distinct=True), 
    ).order_by('-created_at')