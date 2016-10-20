from __future__ import unicode_literals
import os, config, random, math

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError


class Trophy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Powerup(models.Model):
    name = models.CharField(max_length=32, unique=True)
    icon_url = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


# Many-to-many intermediate table
class PlayerTrophy(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    earned = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.player) + " - " + str(self.trophy)


# Many-to-many intermediate table
class PlayerPowerup(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    powerup = models.ForeignKey(Powerup, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return str(self.player) + " - " + str(self.powerup)


class Player(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    icon_filename = models.CharField(max_length=16, null=True, blank=True)
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)  # TODO config class defining xp leveling limits
    played_with = models.ManyToManyField("self", blank=True)

    # Analytical stats
    # Deprecated because of PlayerQuestion model, one can calculate average by looking at that
    # average_time_to_answer_seconds = models.FloatField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "player_" + str(self.pk)

    def update(self, player):
        self.xp = player['xp']
        self.level = math.floor(config.get_level(self.xp))

        print player['powerups']
        for powerup in player['powerups']:
            player_powerup = PlayerPowerup.objects.get(powerup['id'])
            player_powerup.quantity = powerup['quantity']
            player_powerup.save()

        print player['questions_answered']
        for question_answer in player['questions_answered']:
            for player_id in question_answer['player_ids']:
                other_player = Player.objects.get(pk=player_id)
                if other_player != self:
                    self.played_with.add(other_player)

            question = Question.objects.get(pk=question_answer['question_id'])
            PlayerQuestion.objects.get_or_create(player=self, question=question,
                                                 is_correct=question_answer['is_correct'],
                                                 elapsed_time=question_answer['elapsed_time'])

        self.save()

    def set_powerups_and_trophies(self):
        """If a new powerup or trophy is added, a player-powerup link is created for active players"""
        all_powerups = Powerup.objects.all()
        for powerup in all_powerups:
            PlayerPowerup.objects.get_or_create(player=self, powerup=powerup)
            # All new players start with zero powerups

        all_trophies = Trophy.objects.all()
        for trophy in all_trophies:
            PlayerTrophy.objects.get_or_create(player=self, trophy=trophy)
            # All new players start with zero trophies

    def add_xp(self, **kwargs):
        self.xp += int(kwargs['xp']) if 'xp' in kwargs else int(config.DEFAULT_XP)
        self.check_level()
        self.save()

    def set_xp(self, xp):
        self.xp = xp
        self.check_level()
        self.save()

    def check_level(self):  # Checks if current xp warrants a levelup
        self.level = config.get_level(self.xp)

    def set_powerup_quantity(self, powerup_pk, quantity):
        powerup = Powerup.objects.get(pk=powerup_pk)
        player_powerup, created = PlayerPowerup.objects.get_or_create(player=self, powerup=powerup)
        player_powerup.quantity = quantity
        player_powerup.save()

    # TODO earn trophy equal to given pk
    def earn_trophy(self, trophy_pk):
        trophy = Trophy.objects.get(pk=trophy_pk)
        player_trophy, created = PlayerTrophy.objects.get_or_create(player=self, trophy=trophy)
        player_trophy.earned = True
        player_trophy.save()

    def assign_adjective_noun_name_and_icon(self):
        # Get list of currently active names (so no overlap)
        nouns_in_use = []
        badges = Badge.objects.filter(active_player__isnull=False)
        for badge in badges:
            nouns_in_use.append(str(badge.active_player.name).split(" ")[1])

        print "nouns in use"
        print nouns_in_use
        # Generate random pair of adjective-noun, check if is already used, if so try again
        for i in range(0, 10):
            name = {
                "adjective": random.choice(config.adjectives),
                "noun": random.choice(config.nouns_filenames.keys())
            }
            if name['noun'] in nouns_in_use:
                continue
            self.name = str(str(name['adjective']).title() + " " + name['noun'])
            print "icon_filename:"
            self.icon_filename = "animal_icons/" + config.nouns_filenames.get(name['noun']) + config.file_name_postfix
            print self.icon_filename
            print self.name

            self.save()
            return


def player_saved(sender, created, instance, *args, **kwargs):
    instance.set_powerups_and_trophies()
    if created:
        instance.assign_adjective_noun_name_and_icon()


# After a new player is registered, initial config must be completed
post_save.connect(player_saved, sender=Player)


class Terminal(models.Model):
    name = models.CharField(max_length=32, unique=True)
    online = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def set_online(self):
        if not self.online:
            self.online = True
            return True
        else:
            return False

    def set_offline(self):
        if self.online:
            self.online = False
            return True
        else:
            return False


class Session(models.Model):
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, default=None)
    player_1 = models.ForeignKey(Player, related_name="player_1", on_delete=models.CASCADE)
    player_2 = models.ForeignKey(Player, related_name="player_2", on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name="player_winner", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('terminal', 'player_1'), ('terminal', 'player_2'))

    def __unicode__(self):
        return "Terminal " + str(self.terminal) + " | " + str(self.player_1) + " vs " + str(self.player_2) + \
               ", winner: " + str(self.winner)

    def save(self, *args, **kwargs):  # TODO maybe this should be in a validator
        if self.player_1 == self.player_2:
            raise ValidationError("You cannot play with yourself")
        if self.winner not in [self.player_1, self.player_2]:
            raise ValidationError("Winner must be one of player_1 or player_2")
        all_sessions = Session.objects.all()
        for session in all_sessions:
            if session.terminal == self.terminal:
                if set([session.player_1, session.player_2]) & set([self.player_1, self.player_2]):
                    raise ValidationError("player_1 or player_2 has already completed this terminal")

        super(Session, self).save(*args, **kwargs)


class Badge(models.Model):
    uid = models.CharField(max_length=8, unique=True)
    active_player = models.ForeignKey(Player, null=True, blank=True)  # If this is null badge is available

    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.uid


class Question(models.Model):
    text = models.CharField(max_length=512)
    hint = models.CharField(max_length=128)
    left_picture_url = models.CharField(max_length=64)
    right_picture_url = models.CharField(max_length=64)
    is_left_correct = models.BooleanField()
    terminal = models.ForeignKey(Terminal)

    def __unicode__(self):
        return "question_" + str(self.id)


class PlayerQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    elapsed_time = models.FloatField()

    class Meta:
        unique_together = ('question', 'player')

    def __unicode__(self):
        return str(self.question) + ":" + str(self.player) + ", correct: " + str(self.is_correct)

