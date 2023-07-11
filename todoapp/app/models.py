from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey('users.CustomUser', null=False, on_delete=models.CASCADE)
    body = models.CharField(max_length=255, null=False)
    like = models.ManyToManyField("users.CustomUser", related_name='like_comment')
    date_create = models.DateTimeField()

class Post(models.Model):
    author = models.ForeignKey('users.CustomUser', null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=155, null=False)
    body = models.TextField(null=True)
    like = models.ManyToManyField("users.CustomUser", related_name='like_post')
    header_image = models.ImageField(upload_to='media/', null=True, blank=True)
    comments = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    slug = AutoSlugField(populate_from='title', unique=True)


class Feedback(models.Model):
    author = models.ForeignKey('users.CustomUser', null=False, on_delete=models.CASCADE)
    email = models.EmailField(null=False)
    body = models.TextField(max_length=255)
    title = models.CharField(max_length=155)

