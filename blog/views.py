from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    def get_queryset(self):
        return Post.objects.filter(sign=True).order_by('created_at')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/post_add.html'
    success_url = reverse_lazy('blog:posts')
