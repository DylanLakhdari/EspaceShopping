from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    pass
    email = models.EmailField(
        error_messages={'unique': 'Cet email existe déjà'}, unique=True)
    
    first_name = models.CharField(
        max_length=150,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'Le prénom doit uniquement contenir des lettres.')],
        blank=True
    )

    last_name = models.CharField(
        max_length=150,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'Le nom doit uniquement contenir des lettres.')],
        blank=True
    )

    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username