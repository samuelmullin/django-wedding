from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Meal(models.model):
	name = models.CharField(max_length=50, blank=False)
	description = models.CharField(max_length=200, blank=False)

class Guest(models.model):
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	email = models.EmailField(blank=False)
	phone = models.CharField(max_length=20, blank=False)
	meal_preference = models.CharField(max_length=50, blank=False)
	rsvp = models.BooleanField(default=False)
	text = models.TextField(blank=True)

class Party(models.model):
	num_adults = models.IntegerField(default=1, null=False)
	num_kids = models.IntegerField(default=0, null=False)
	main_contact = models.ForeignKey(Guest)
	secondary_contact = models.ManyToOneField(Guest)
