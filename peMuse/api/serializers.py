from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerup, Trophy


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup
        fields = ('name', 'description', 'url')
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
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


class PlayerSerializer(serializers.ModelSerializer):
    trophies = TrophySerializer(source='get_trophies', many=True, read_only=True)
    powerups = PlayerPowerupSerializer(source='playerpowerup_set', many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('uid', 'xp', 'level', 'url', 'trophies', 'powerups', 'played_with')
        lookup_field = 'uid'
        extra_kwargs = {
            'url': {'lookup_field': 'uid'}
        }
