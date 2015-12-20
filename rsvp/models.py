from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Meal(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)


class Accommodation(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)


class Guest(models.Model):
    rsvp = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    rsvp_date = models.DateField(default=timezone.now)
    meal_preference = models.CharField(max_length=50, blank=True, default='')
    accom_preference = models.CharField(max_length=50, blank=True, default='')
    text = models.TextField(blank=True, default='')
    party = models.ForeignKey("Guest")
