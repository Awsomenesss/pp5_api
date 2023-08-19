from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    belt_choices = [
        ("white", "White"),
        ("blue", "Blue"),
        ("purple", "Purple"),
        ("brown", "Brown"),
        ("black", "Black"),
    ]
    belt_color = models.CharField(
        max_length=32, choices=belt_choices, blank=False, default='white'
    )

    gi_or_no_gi_choices = [
        ("gi", "Gi"),
        ("no_gi", "No Gi"),
    ]
    gi_or_no_gi = models.CharField(
        max_length=32, choices=gi_or_no_gi_choices, blank=False, null=True
    )
    years_trained = models.PositiveIntegerField(default=0)
    profile_image = models.ImageField(
        upload_to='images/', default='../default_profile_o5f3a0', blank=True
    )
    introduction = models.TextField(
        null=True, blank=True, verbose_name="Personal Introduction")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
