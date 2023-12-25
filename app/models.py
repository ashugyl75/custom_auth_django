from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=20, null=True, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    dob = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username