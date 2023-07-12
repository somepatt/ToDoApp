from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView

from .forms import *
from .models import *
# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'home_page.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        return context
    

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class AboutPage(TemplateView):
    template_name = 'about_page.html'


class PostPage(DetailView):             #доделать
    model = Post
    template_name = 'post_page.html'
    slug_url_kwarg = 'post_slug'    
    context_object_name = 'post'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home_page')           #на страницу поста

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            Post.objects.create(**form.cleaned_data)
            return redirect('home_page')
        return redirect('add_post')