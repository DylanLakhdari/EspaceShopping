from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    email = models.EmailField(
        error_messages={'unique': 'Cet email existe déjà'}, unique=True)

    def __str__(self):
        return self.username