# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_badge_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='created_at',
        ),
    ]