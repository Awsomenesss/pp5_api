from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    introduction = serializers.CharField(allow_blank=True, required=False)
    belt_color = serializers.ChoiceField(choices=Profile.belt_choices, required=False)
    gi_or_no_gi = serializers.ChoiceField(choices=Profile.gi_or_no_gi_choices, required=False)
    years_trained = serializers.IntegerField(min_value=0, required=False)
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    event_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    profile_image = serializers.ImageField(required=False, allow_null=True)
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at', 'name',
            'introduction', 'belt_color', 'gi_or_no_gi', 'years_trained', 'following_id', 'posts_count', 'event_count', 'followers_count', 'following_count', 'profile_image',
        ]
