# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='icon_filename',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
