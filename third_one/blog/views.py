from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):   #class for home site
    model = Post
    template_name = 'home.html'
    context_object_name = 'home'
class BlogDetailView(DetailView):   #class for Post site with detail about post
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'