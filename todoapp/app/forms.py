from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    header_image = forms.ImageField(label='Изображение')
    title = forms.CharField(label='Название')
    body = forms.CharField(widget=forms.Textarea, label='')
    is_published = forms.BooleanField(label='Опубликовать')

    class Meta:
        model = Post
        fields = (
            'header_image',
            'title',
            'body',
            'is_published'
        )


class AddCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите комментарий'}))

    class Meta:
        model = Comment
        fields = ('body',)