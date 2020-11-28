from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER      = (
        ('', 'Select Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    USER_ROLE    = (
        ('', 'Select a Role'),
        ('M', 'Moderator'),
        ('S', 'Student'),
        ('L', 'Landlord')
    )

    role         = models.CharField(max_length=9, default='', choices=USER_ROLE)  
    gender       = models.CharField(max_length=6, choices=GENDER, default='')
    address      = models.CharField(max_length=255)
    phone        = models.CharField(max_length=10)
    email        = models.EmailField(max_length=100, unique=True)
    date_of_birth= models.DateField(blank=True, null=True)
    image        = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)






    # def __str__(self):
    #     return f'Profile for user {self.user.username}'