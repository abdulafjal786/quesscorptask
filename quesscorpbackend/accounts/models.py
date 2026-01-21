from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=50,
        choices=USER_TYPE_CHOICES,
        default='employee'
    )

    def __str__(self):
        return self.username
