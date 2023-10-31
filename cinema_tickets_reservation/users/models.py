from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('CONSUMER', 'Consumer'),
        ('SUPER_USER', 'Super User'),
    )
    
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='CONSUMER')
    email = models.EmailField(('email address'), unique=True)  # Make email unique
    phone_number = models.CharField(max_length=15, null=True, blank=True)
