from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    is_team = models.BooleanField(default=False)
    num_member = models.IntegerField(default=0)
    