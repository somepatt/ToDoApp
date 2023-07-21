from django.urls import path, include

from .views import *

app_name = 'app'

url_app_pattern = [
    path('', HomePage.as_view(), name='home_page'),
    path('post/addpost/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', PostPage.as_view(), name='post_url'),
    path('post/<slug:post_slug>/update/', UpdateView.as_view(), name='update_post_url'),
    path('post/<slug:post_slug>/delete/', DeletePostView.as_view(), name='delete_post_url'),
    path('post/<slug:post_slug>/like/', LikeView, name='like_post_url'),
    path('post/result/search/', SearchForm, name='search_url'),
    path('post/<slug:post_slug>/like/<int:comment_id>/', LikeCommentView, name='like_comment_url'),
]