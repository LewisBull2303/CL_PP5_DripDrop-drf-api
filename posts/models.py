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