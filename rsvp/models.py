from __future__ import unicode_literals

from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)


class Guest(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    rsvp_date = models.DateField(auto_now_add=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    meal_preference = models.CharField(max_length=50, blank=False)
    primary_contact = models.BooleanField(default=True)
    rsvp = models.BooleanField(default=False)
    text = models.TextField(blank=True)


class Party(models.Model):
    num_adults = models.IntegerField(default=1, null=False)
    num_kids = models.IntegerField(default=0, null=False)
    contact = models.ForeignKey(Guest, related_name='party')
    text = models.TextField(blank=True)
