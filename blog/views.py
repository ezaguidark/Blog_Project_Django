from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Por alguna razon, las clases de abajo tambien las podia importar directamente de django.views.generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'img']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')