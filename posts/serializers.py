from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from posts.models import Post
from likes.models import PostLike 
from dislikes.models import PostDislike 
from comments.models import Comment  

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    like_id = serializers.SerializerMethodField()
    dislike_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    dislikes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

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
            like = PostLike.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None
    def get_dislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dislike = PostDislike.objects.filter(
                owner=user, post=obj
            ).first()
            return dislike.id if dislike else None
        return None   
    def get_comment_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment = Comment.objects.filter(
                owner=user, event=obj
            ).first()
            return comment.id if comment else None
        return None 

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter', 'like_id', 'dislike_id','likes_count','dislikes_count', 'comments_count',
        ]