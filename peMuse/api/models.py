from __future__ import unicode_literals
from django.db import models


# A powerup
class Powerup(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Trophy(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


# Create your models here.
class Player(models.Model):
    uid = models.CharField(max_length=32)  # TODO set this to 8
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)  # TODO config class defining xp leveling limits
    powerups = models.ManyToManyField(Powerup, through='PlayerPowerups', null=True, blank=True)
    trophies = models.ManyToManyField(Trophy, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")+" - "+self.uid


# Intermediary class counting powerups since that is the only way to have multiples (Quantity)
class PlayerPowerups(models.Model):
    powerup = models.ForeignKey(Powerup)
    player = models.ForeignKey(Player)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return str(self.powerup.name + ', quantity: ' + self.quantity)
