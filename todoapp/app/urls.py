from django.urls import path

from .views import *

url_app_pattern = [
    path('', HomePage.as_view(), name='home_page'),
    path('addpost', AddPost.as_view(), name='add_post')
]