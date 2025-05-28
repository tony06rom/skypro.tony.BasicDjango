from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView


app_name = BlogConfig.name


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path("post_add/", PostCreateView.as_view(),name="post_add")
]
