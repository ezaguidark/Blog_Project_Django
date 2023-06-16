from django.urls import path # esto va basicamente en todos los urls.py
from .views import BlogListView, BlogDetailView, BlogCreateView # aqui van todas las views de la app

urlpatterns = [
    path('', BlogListView.as_view(), name= 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
]