from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    resdential_address = models.CharField(max_length=200, null=False, blank=False)
    mobile_number = models.BigIntegerField(null=False, blank=False)


