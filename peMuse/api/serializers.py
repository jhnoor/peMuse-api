from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerups, Trophy


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup
        fields = ('name', 'description')


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ('name', 'description')


class PlayerSerializer(serializers.ModelSerializer):
    trophies = TrophySerializer(many=True)
    #powerups = PlayerPowerupsSerializer(many=True, null=True, blank=True)

    class Meta:
        model = Player


class PlayerPowerupsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    powerups = PowerupSerializer(many=True)

    class Meta:
        model = PlayerPowerups
        fields = ('player', 'powerup', 'quantity')
