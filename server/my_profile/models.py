from django.db import models

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    key_walmart = models.CharField(max_length=40, blank=True)
