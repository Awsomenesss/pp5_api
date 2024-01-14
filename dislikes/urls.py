from django.urls import path
from dislikes import views

urlpatterns = [
    # URLs for PostDislike
    path('post-dislikes/', views.PostDislikeList.as_view(), name='post-dislike-list'),
    path('post-dislikes/<int:pk>/', views.PostDislikeDetail.as_view(), name='post-dislike-detail'),

    # URLs for EventDislike
    path('event-dislikes/', views.EventDislikeList.as_view(), name='event-dislike-list'),
    path('event-dislikes/<int:pk>/', views.EventDislikeDetail.as_view(), name='event-dislike-detail'),
]