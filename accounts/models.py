from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

