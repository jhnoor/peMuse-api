from __future__ import unicode_literals
from django.db import models


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


# Intermediary class counting powerups since that is the only way to have multiples (Quantity)
class PlayerPowerup(models.Model):
    player = models.ForeignKey('Player')  # TODO on_delete=models.CASCADE
    powerup = models.ForeignKey(Powerup)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.player.uid + " - " + self.powerup.name


# Create your models here.
class Player(models.Model):
    uid = models.CharField(max_length=32)  # TODO set this to 8
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)  # TODO config class defining xp leveling limits
    powerups = models.ManyToManyField(Powerup, through='PlayerPowerup')
    trophies = models.ManyToManyField(Trophy)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S") + " - " + self.uid

    def get_trophies(self):
        return self.trophies.order_by("name")

    def get_powerups(self):
        return self.powerups.order_by("name")
