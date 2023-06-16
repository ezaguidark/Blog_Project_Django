from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    # Los parametros en fields deben tener los mismos nombres que en Models.py
    fields = ['title', 'author', 'body', 'img'] 