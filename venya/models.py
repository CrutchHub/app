from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    phone = models.PhoneNumberField(null=False, blank=False, unique=True)