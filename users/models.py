from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # We can add more fields here later (e.g., is_freelancer)

    # Use email for login instead of username? (Optional, but modern)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.username