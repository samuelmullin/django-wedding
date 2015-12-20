# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20151219_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='accom_preference',
        ),
        migrations.AddField(
            model_name='party',
            name='accom_preference',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='party',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]