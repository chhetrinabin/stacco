from django.db import models
from django.contrib.auth.models import AbstractUser
from account.models import User
from django.conf import settings
from django.utils.text import slugify 



class Advertisement(models.Model):
    STATUS_CHOICES = (
        ('', 'Select ads status'),
        ('Inactive', 'Inactive'),
        ('Under-Review', 'Under-Review'),
        ('Active', 'Active'),
    )

    ROOM_SIZE            = (
        ('','Select room size'),
        ('Small','Small',),
        ('Medium','Medium',),
        ('Large','Large',)
    )
    advertisement_title              = models.CharField(max_length=255, null=True)
    advertisement_slug               = models.SlugField(unique=True)
    advertiser                       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advertisement_description        = models.TextField()
    room_size                        = models.CharField(max_length=6, choices=ROOM_SIZE, default='')
    no_of_rooms_available            = models.PositiveIntegerField(null=True, blank=False)
    date_of_availability             = models.DateTimeField(auto_now=True)
    address                          = models.CharField(max_length=255, null=True)
    suburb                           = models.CharField(max_length=100, null=True)
    nearby_landmark                  = models.CharField(max_length=100)
    weekly_rent                      = models.PositiveIntegerField(null=True, blank=False)
    bond_amount_required             = models.PositiveIntegerField(null=True, blank=False)
    advertisement_pictures           = models.ImageField(upload_to='ads_images/% Y/% m/% d/', null=False)
    ads_approval_status  = models.BooleanField(default=False)
    ads_status           = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactivec', editable=True)
    ads_total_views      = models.PositiveIntegerField(default=0)
    ads_date_created     = models.DateTimeField(auto_now_add=True)
    ads_date_updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        


class Favourite(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_Favourite  = models.BooleanField(default=False)

    def __str__(self):
        return self.status


class Feedback(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    feedback      = models.TextField()
    reason        = models.TextField()
    moderator     = models.ForeignKey("account.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.feedback