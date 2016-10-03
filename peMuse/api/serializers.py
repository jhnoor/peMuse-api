from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerup, Trophy, PlayerTrophy


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup
        fields = ('name', 'description', 'url')
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class PlayerPowerupSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='powerup.name')  # Accessing the model
    description = serializers.ReadOnlyField(source='powerup.description')

    class Meta:
        model = PlayerPowerup
        fields = ('name', 'description', 'quantity', 'url')


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ('name', 'description', 'url')
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class PlayerTrophySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='trophy.name')  # Accessing the model
    description = serializers.ReadOnlyField(source='trophy.description')

    class Meta:
        model = PlayerTrophy
        fields = ('name', 'description', 'earned', 'player', 'url')

class PlayerSerializer(serializers.ModelSerializer):
    trophies = PlayerTrophySerializer(source='playertrophy_set', many=True, read_only=True)
    powerups = PlayerPowerupSerializer(source='playerpowerup_set', many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('xp', 'level', 'url', 'trophies', 'powerups', 'played_with')
