from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import ListView , DetailView, CreateView,UpdateView, DeleteView

from .models import Blog
from .forms import BlogFrom


class BlogView(ListView):
    model = Blog
    template_name = 'blog/all_blogs.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogFrom
    template_name = 'blog/add_post.html'


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogFrom
    template_name = 'blog/update_post.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('all_blogs')
    template_name = 'blog/delete_post.html'