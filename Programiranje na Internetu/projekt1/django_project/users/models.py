from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class Korisnici(AbstractBaseUser):
    email = models.CharField(
                max_length=64,
                unique = True,
            )
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=7)
    status = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'korisnici'