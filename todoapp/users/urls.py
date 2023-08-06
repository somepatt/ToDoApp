from django.urls import path

from .views import *

url_users_pattern = [
    path('login/', LoginUser.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', RegisterUserView.as_view(), name='register_url'),
    path('profile/<slug:user_slug>', ProfileView.as_view(), name='profile_url'),
    path('profile/<slug:user_slug>/update', UpdateProfile.as_view(), name='update_profile_url'),
]
