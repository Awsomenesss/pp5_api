from django.urls import path
from comments import views

urlpatterns = [
    # URLs for Postscomments
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),

    # URLs for Eventcomments
    path('event-comments/', views.EventCommentList.as_view(), name='event-comment-list'),
    path('event-comments/<int:pk>/', views.EventCommentDetail.as_view(), name='event-comment-detail'),
]
