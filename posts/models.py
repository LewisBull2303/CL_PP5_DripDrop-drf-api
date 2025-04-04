# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Post(models.Model):
    """
    A class for the post model
    """
    category_choices = [
    ('Classic Casual', 'Classic Casual'),
    ('Sporty (Athleisure)', 'Sporty (Athleisure)'),
    ('Streetwear', 'Streetwear'),
    ('Bohemian (Boho)', 'Bohemian (Boho)'),
    ('Preppy', 'Preppy'),
    ('Hipster', 'Hipster'),
    ('Grunge', 'Grunge'),
    ('Minimalist', 'Minimalist'),
    ('Y2K Fashion', 'Y2K Fashion'),
    ('Soft Girl', 'Soft Girl'),
    ('VSCO Girl', 'VSCO Girl'),
    ('Cottagecore', 'Cottagecore'),
    ('E-Girl', 'E-Girl'),
    ('Skater', 'Skater'),
    ('Dark Academia', 'Dark Academia'),
    ('Light Academia', 'Light Academia'),
    ('Indie', 'Indie'),
    ('Business Casual', 'Business Casual'),
    ('Business Professional', 'Business Professional'),
    ('Smart Casual', 'Smart Casual'),
    ('Power Dressing', 'Power Dressing'),
    ('Punk', 'Punk'),
    ('Gothic', 'Gothic'),
    ('Cyberpunk', 'Cyberpunk'),
    ('Rockstar Chic', 'Rockstar Chic'),
    ('Steampunk', 'Steampunk'),
    ('Emo', 'Emo'),
    ('Gyaru', 'Gyaru'),
    ('Vintage', 'Vintage'),
    ('Retro', 'Retro'),
    ('Kawaii', 'Kawaii'),
    ('Harajuku', 'Harajuku'),
    ('Lolita', 'Lolita'),
    ('K-Pop Fashion', 'K-Pop Fashion'),
    ('Hippie', 'Hippie'),
    ('Winter Fashion', 'Winter Fashion'),
    ('Summer Fashion', 'Summer Fashion'),
    ('Resort Wear', 'Resort Wear'),
    ('Workwear (Utility Fashion)', 'Workwear (Utility Fashion)'),
    ('Avant-Garde', 'Avant-Garde'),
    ('Haute Couture', 'Haute Couture'),
    ('Luxury Chic', 'Luxury Chic'),
    ('Sci-Fi/Fantasy Fashion', 'Sci-Fi/Fantasy Fashion'),
    ('Rave/Festival Fashion', 'Rave/Festival Fashion'),
    ('Normcore', 'Normcore'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=category_choices)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_umaui6',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'