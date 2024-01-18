from django.urls import path
from dislikes import views

urlpatterns = [
    # URLs for PostDislike
    path('post-dislikes/', views.PostDislikeList.as_view()),
    path('post-dislikes/<int:pk>/', views.PostDislikeDetail.as_view()),

    # URLs for EventDislike
    path('event-dislikes/', views.EventDislikeList.as_view()),
    path('event-dislikes/<int:pk>/', views.EventDislikeDetail.as_view()),
]