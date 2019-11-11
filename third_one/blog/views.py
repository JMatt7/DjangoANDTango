from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class BlogListView(ListView):   #class for home site
    model = Post
    template_name = 'home.html'
    context_object_name = 'home'
class BlogDetailView(DetailView):   #class for Post site with detail about post
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['author', 'title', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')