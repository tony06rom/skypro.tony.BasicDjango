from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

app_name = BlogConfig.name


urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post"),
    path("post_update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("post_add/", PostCreateView.as_view(), name="post_add"),
    path("post_del/<int:pk>", PostDeleteView.as_view(), name="post_del"),
]
