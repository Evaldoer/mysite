from django.urls import path
from .views import PostView, PostListView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='hello'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]