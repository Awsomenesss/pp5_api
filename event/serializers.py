from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from event.models import Event
from likes.models import EventLike  

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = EventLike.objects.filter(
                owner=user, event=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at', 'image', 'description',
            'date', 'time', 'location', 'like_id', 'likes_count', 
        ]