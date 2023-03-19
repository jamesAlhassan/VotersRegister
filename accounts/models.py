from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    
    last_name = models.CharField(max_length=200, null=False, blank=False)

    date_of_birth = models.DateField(max_length=8)
    
    age = models.PositiveIntegerField(null=False, blank=False)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    
    resdential_address = models.CharField(max_length=200, null=False, blank=False)
    
    mobile_number = models.BigIntegerField(null=False, blank=False)

    
    def calculate_age(self, born):
        today = date.today()
        born = self.date_of_birth.year

        try: 
            birthday = self.date_of_birth.replace(year=today.year)
        # raised when birth date is February 29 and the current year is not a leap year
        except ValueError:
            birthday = self.date_of_birth.replace(year=today.year, day=born.day-1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year
