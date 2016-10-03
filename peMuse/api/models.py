from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save


class Trophy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Powerup(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


# Many-to-many intermediate table
class PlayerTrophy(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    earned = models.BooleanField(default=False)

    def __unicode__(self):
        return self.player.uid + " - " + self.trophy.name


# Many-to-many intermediate table
class PlayerPowerup(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    powerup = models.ForeignKey(Powerup, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.player.uid + " - " + self.powerup.name


class Player(models.Model):
    uid = models.CharField(max_length=32, unique=True)  # TODO set this to 8
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)  # TODO config class defining xp leveling limits
    played_with = models.ManyToManyField("self", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S") + " - " + self.uid

    def init_player_powerups(self):
        all_powerups = Powerup.objects.all()
        for powerup in all_powerups:
            player_powerup = PlayerPowerup(player=self, powerup=powerup)  # All new players start with zero powerups
            player_powerup.save()

    def init_player_trophies(self):
        all_trophies = Trophy.objects.all()
        for trophy in all_trophies:
            player_trophy = PlayerTrophy(player=self, trophy=trophy)
            player_trophy.save()

    # TODO add_xp(), random_powerup(), earn_trophy()


def player_saved(sender, instance, *args, **kwargs):
    instance.init_player_powerups()
    instance.init_player_trophies()


# After a new player is registered, initial config must be completed
post_save.connect(player_saved, sender=Player)
