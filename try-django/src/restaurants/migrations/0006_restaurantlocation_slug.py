# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-26 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20180726_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
