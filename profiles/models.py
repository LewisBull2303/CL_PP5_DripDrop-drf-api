# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Profile(models.Model):
    """
    A class for the profile model
    User gets automatically created via
    signal when the user creates their account
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../Default_pfp_nxyoza'
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        """
        Return information who the profile owner is
        """
        return f"{self.owner}'s profile"
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(owner=instance)


    post_save.connect(create_profile, sender=User)