from django import forms

from .models import *
#формы
class AddPostForm(forms.Model):
    header_image = forms.ImageField()
    title = forms.CharField()
    body = forms.CharField(widget=forms.TextInput)
    is_published = forms.BooleanField()
    class Meta:
        model = Post
        fields = ('header_image', 'title', 'body', 'is_published')