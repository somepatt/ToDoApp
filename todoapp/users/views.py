from typing import Any, Optional
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from .forms import *
# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterCustomUser
    template_name = 'register_user.html'
     
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_page')                #поменять на профиль
    

class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'login_user.html'
    success_url = reverse_lazy('home_page')         #поменять на профиль


class UpdateProfile(UpdateView):
    form_class = UpdateUserForm
    template_name = 'update_user.html'        #поменять на профиль

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customuser"] = self.request.user
        return context
    
    def put(self, request, user_slug):
        print('put')
        form = UpdateUserForm(request.PUT, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_url', user_slug)

    def get_object(self):
        return self.request.user
    
    

class ResetPassword(UpdateView):
    form_class = ChangePasswordUser
    template_name = 'change_password.html'
    success_url = reverse_lazy('home_page')         #поменять на профиль


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'profile_page.html'
    context_object_name = 'customuser'
    slug_url_kwarg = 'user_slug'