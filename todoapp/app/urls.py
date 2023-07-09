from django.urls import path

from .views import *

url_app_pattern = [
    path('', main)
]