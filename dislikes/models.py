from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from event.models import Event

class PostDislike(models.Model):
    """
    PostDislike model, related to 'owner' and 'post'.
    'owner' is a User instance, 'post' is a Post instance.
    Ensures a user can't dislike the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_dislikes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} disliked post {self.post.id}'

class EventDislike(models.Model):
    """
    EventDislike model, related to 'owner' and 'event'.
    'owner' is a User instance, 'event' is an Event instance.
    Ensures a user can't dislike the same event twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_dislikes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} disliked event {self.event.id}'
