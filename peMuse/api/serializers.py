from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerup, Trophy


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup
        fields = ('name', 'description')


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ('name', 'description')


class PlayerSerializer(serializers.ModelSerializer):
    trophies = TrophySerializer(source='get_trophies', many=True)
    powerups = PowerupSerializer(source='get_powerups', many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('uid', 'xp', 'level', 'trophies', 'powerups')
