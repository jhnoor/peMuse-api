from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save


class Powerup(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Trophy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


# Intermediary class counting powerups since that is the only way to have multiples (Quantity)
class PlayerPowerup(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)  # TODO on_delete=models.CASCADE
    powerup = models.ForeignKey(Powerup, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.player.uid + " - " + self.powerup.name


# Create your models here.
class Player(models.Model):
    uid = models.CharField(max_length=32, unique=True)  # TODO set this to 8
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)  # TODO config class defining xp leveling limits
    trophies = models.ManyToManyField(Trophy, blank=True)

    played_with = models.ManyToManyField("self", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S") + " - " + self.uid

    def get_trophies(self):
        return self.trophies.order_by("name")

    def init_player_powerups(self):
        all_powerups = Powerup.objects.all()
        print str(all_powerups)
        for powerup in all_powerups:
            player_powerup = PlayerPowerup(player=self, powerup=powerup) # All new players start with zero powerups
            print str(player_powerup)
            player_powerup.save()

    # def init_player_trophies(self): TODO make trophies similar to powerups and have field "earned" default to false


def player_saved(sender, instance, *args, **kwargs):
    instance.init_player_powerups()

# After a new player is registered, initial config must be completed
post_save.connect(player_saved, sender=Player)
