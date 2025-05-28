from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/posts.html"

    def get_queryset(self):
        return Post.objects.filter(sign=True).order_by("created_at")


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post.html"

    def get_object(self):
        post = Post.objects.get(pk=self.kwargs["pk"])
        post.views_cnt += 1
        post.save()
        return post


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "image", "sign"]
    template_name = "blog/post_add.html"
    success_url = reverse_lazy("blog:posts")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "image", "sign"]
    template_name = "blog/post_update.html"

    def get_success_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_del.html"
    success_url = reverse_lazy("blog:posts")
