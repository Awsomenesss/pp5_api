from django.urls import path
from likes import views

urlpatterns = [
    # URLs for PostLike
    path('post-likes/', views.PostLikeList.as_view()),
    path('post-likes/<int:pk>/', views.PostLikeDetail.as_view()),

    # URLs for EventLike
    path('event-likes/', views.EventLikeList.as_view()),
    path('event-likes/<int:pk>/', views.EventLikeDetail.as_view()),
]