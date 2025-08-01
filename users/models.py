from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can extend with more fields later
    pass
