from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    

class CustomUser(AbstractUser):

    date_of_birth = models.DateField(null=True, blank=True)
    
    age = models.PositiveIntegerField(null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    
    residential_address = models.CharField(max_length=200,null=True, blank=True)
    
    mobile_number = models.IntegerField(null=True, blank=True, unique=True)

    def get_age(self):
        age = date.today()-self.date_of_birth
        return int((age).days/365.25)