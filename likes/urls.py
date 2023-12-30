from django.urls import path
from likes import views

urlpatterns = [
    # URLs for PostLike
    path('post-likes/', views.PostLikeList.as_view(), name='post-like-list'),
    path('post-likes/<int:pk>/', views.PostLikeDetail.as_view(), name='post-like-detail'),

    # URLs for EventLike
    path('event-likes/', views.EventLikeList.as_view(), name='event-like-list'),
    path('event-likes/<int:pk>/', views.EventLikeDetail.as_view(), name='event-like-detail'),
]