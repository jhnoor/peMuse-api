# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 01:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_playerquestion_elapsed_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='average_time_to_answer_seconds',
        ),
        migrations.RemoveField(
            model_name='player',
            name='total_playtime_seconds',
        ),
        migrations.AlterUniqueTogether(
            name='playerquestion',
            unique_together=set([('question', 'player')]),
        ),
    ]
