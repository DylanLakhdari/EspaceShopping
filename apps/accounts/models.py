from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username