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
    template_name = 'update_user.html'
    success_url = reverse_lazy('home_page')         #поменять на профиль


class ResetPassword(UpdateView):
    form_class = ChangePasswordUser
    template_name = 'change_password.html'
    success_url = reverse_lazy('home_page')         #поменять на профиль