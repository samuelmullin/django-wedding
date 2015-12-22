from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Meals():
    CHICKEN = 'chicken'
    VEG = 'veg'
    FISH = 'fish'

    choices = (
        (CHICKEN, 'chicken'),
        (VEG, 'veg'),
        (FISH, 'fish'),
    )


class Accoms():

    HOTEL = 'hotel'
    HUT = 'hut'
    CASTLE = 'castle'

    choices = (
        (HOTEL, 'Hotel'),
        (HUT, 'Hut'),
        (CASTLE, 'Fish'),
    )


class Guest(models.Model):
    rsvp = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    rsvp_date = models.DateField(default=timezone.now)
    meal_preference = models.CharField(max_length=50, choices=Meals.choices)
    accom_preference = models.CharField(max_length=50, choices=Accoms.choices)
    text = models.TextField(blank=True, default='')
    kid = models.BooleanField(default=False)
    party = models.ForeignKey("Guest", null=True)

    def __unicode__(self):
        return self.name

