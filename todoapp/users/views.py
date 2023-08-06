from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import *


# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterCustomUser
    template_name = 'register_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # TODO: поменять на профиль
        return redirect('home_page')


class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'login_user.html'
    # TODO: поменять на профиль
    success_url = reverse_lazy('home_page')


class UpdateProfile(UpdateView):
    form_class = UpdateUserForm
    # TODO: поменять на профиль
    template_name = 'update_user.html'

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
    # TODO: поменять на профиль
    success_url = reverse_lazy('home_page')


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'profile_page.html'
    context_object_name = 'customuser'
    slug_url_kwarg = 'user_slug'
