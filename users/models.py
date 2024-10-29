from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'admin'
    READER = 'reader'
    USER_TYPES = [
        (ADMIN, 'Administrador'),
        (READER, 'Leitor'),
    ]

    user_type = models.CharField(max_length=13, choices=USER_TYPES, default=READER)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username