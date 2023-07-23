from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .alghoritms import *
from .forms import *
from .models import *
# Create your views here.
class HomePage(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home_page.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('users:login_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        return context
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class AboutPage(LoginRequiredMixin, TemplateView):
    template_name = 'about_page.html'
    login_url = reverse_lazy('users:login_url')


class PostPage(LoginRequiredMixin, DetailView):             #доделать
    model = Post
    template_name = 'post_page.html'
    slug_url_kwarg = 'post_slug'
    pk_url_kwarg = 'post_id'    
    context_object_name = 'post'
    login_url = reverse_lazy('users:login_url')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        context['form'] = AddCommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            pk = Post.objects.get(slug=kwargs['post_slug']).pk
            form.cleaned_data['post_id'] = pk
            Comment.objects.create(**form.cleaned_data)
        return redirect('app:post_url', kwargs['post_slug'])
    
    # def form_valid(self, form):
    #     form['author'] = self.request.user
    #     form['post_id'] = self.kwargs['pk']
    #     form.save()
    #     return redirect('post_url', self.kwargs['post_slug'])    


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home_page')           #на страницу поста
    login_url = reverse_lazy('users:login_url')

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            Post.objects.create(**form.cleaned_data)
            return redirect('app:home_page')


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('app:home_page')
    slug_url_kwarg = 'post_slug'
    login_url = reverse_lazy('users:login_url')

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['post_slug'])
        post.delete()
        return redirect('app:home_page')


def LikeView(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if post.like.filter(pk=request.user.pk).exists():
        post.like.remove(request.user)
    else: 
        post.like.add(request.user)
    return redirect('app:post_url', post_slug)

def LikeCommentView(request, post_slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.like.filter(pk=request.user.pk).exists():
        comment.like.remove(request.user)
    else:
        comment.like.add(request.user)
    return redirect('app:post_url', post_slug)


def SearchForm(request):
    search_query = request.GET.get('q')
    if search_query:
        # items = Post.objects.filter(Q(body__icontains=search_query) | Q(title__icontains=search_query))
        items = Post.objects.values_list('title', flat=True)
        result = tolerant_search(search_query, items)
        posts = Post.objects.filter(Q(title__in=[res[0] for res in result]) | Q(body__in=[res[0] for res in result]))
        return render(request, 'search_result.html', {'posts': posts, 'query': search_query, 'customuser': request.user})
    return render(request, 'search_result.html', {'customuser': request.user})


class ChangePostView(LoginRequiredMixin, UpdateView):
    form_class = ChangePostForm
    template_name = 'change_post.html'
    login_url = reverse_lazy('users:login_url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        return context

    def put(self, request, post_slug):
        print('пут')
        form = ChangePostForm(request.PUT, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:post_url', post_slug)

    def get_object(self):
        obj = get_object_or_404(Post, slug=self.kwargs.get('post_slug'))
        return obj
    

def DeleteComment(request, post_slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('app:post_url', post_slug)