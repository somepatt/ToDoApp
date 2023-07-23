from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm

from .models import *
#формы
class RegisterCustomUser(UserCreationForm):
    username = forms.CharField(label='Никнейм')
    email = forms.EmailField(label='Почта')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
    

class UpdateUserForm(UserChangeForm):
    head_image = forms.ImageField(label='Аватар')
    username = forms.CharField(label='Никнейм')
    bio = forms.Textarea()
    email = forms.EmailField(label='Почта')
    date_b = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ('head_image', 'username', 'bio', 'email', 'date_b')


class ChangePasswordUser(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')