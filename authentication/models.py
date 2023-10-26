from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campo personalizado para el email
    email = models.EmailField(unique=True)

    # Otros campos personalizados si es necesario

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'custom_user'
