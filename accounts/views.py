from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # <-- me gustaria investigar mas sobre estas forms
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

""" Por alguna razon, el autor del libro en esta parte importo CreateView
de esta manera. La cosa es que se podria imprtar tal cual como se importaron
todas las clases de views en la blog/views.py y tambien se podria decir que 
imporara todo: 'import *' pero seguire el ejemplo del libro."""

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'