from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from event.models import Event


class Like(models.Model):
    """
    Like model, related to 'owner', 'post', and 'event'.
    'owner' is a User instance, 'post' is a Post instance, and 'event' is an Event instance.
    'unique_together' ensures a user can't like the same post or event twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} {self.post} {self.event}'
