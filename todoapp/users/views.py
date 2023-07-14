from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterCustomUser
    template_name = 'register_user.html'
     
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('app:home_page')                #поменять на профиль
    

class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'login_user.html'
    success_url = reverse_lazy('app:home_page')         #поменять на профиль


class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = UpdateUserForm
    template_name = 'update_user.html'        #поменять на профиль
    login_url = reverse_lazy('users:login_url')

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, slug=kwargs['user_slug'])

        if request.user != user:
            return redirect('app:home_page')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        return context
    
    def put(self, request, user_slug):
        print('put')
        form = UpdateUserForm(request.PUT, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile_url', user_slug)

    def get_object(self):
        return self.request.user
    
    

class ResetPassword(LoginRequiredMixin, UpdateView):
    form_class = ChangePasswordUser
    template_name = 'change_password.html'
    success_url = reverse_lazy('app:home_page')         #поменять на профиль
    login_url = reverse_lazy('users:login_url')

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile_page.html'
    context_object_name = 'customuser'
    slug_url_kwarg = 'user_slug'