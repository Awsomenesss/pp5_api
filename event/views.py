from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from bjj_api.permissions import IsOwnerOrReadOnly


class EventList(APIView):
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        """Retrieve a list of all events."""
        events = Event.objects.all()
        serializer = EventSerializer(
            events, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """Create a new event."""
        serializer = EventSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class EventDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer

    def get_object(self, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(
            event, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)