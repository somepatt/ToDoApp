from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=255, null=True, blank=True)
    date_b = models.DateField(null=True, blank=True)
    slug = AutoSlugField(populate_from='username', unique=True)
    head_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("users:profile_url", kwargs={"user_slug": self.slug})
    