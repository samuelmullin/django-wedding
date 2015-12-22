from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from rsvp.models import Guest


class GuestAdmin(ModelAdmin):
    list_display = ['name', 'party']


admin.site.register(Guest, GuestAdmin)
