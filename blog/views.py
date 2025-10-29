from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from .models import Post

class PostView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'