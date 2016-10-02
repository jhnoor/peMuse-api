from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerup, Trophy


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup
        fields = ('url', 'name', 'description')


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ('url', 'name', 'description')

class PlayerPowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPowerup


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    trophies = TrophySerializer(source='get_trophies', many=True, read_only=True)
    # powerups = PowerupSerializer(source='get_powerups', many=True, read_only=True)
    powerups = serializers.HyperlinkedRelatedField(
        source='get_powerups',many=True, read_only=True, view_name='powerup-detail'
    )

    class Meta:
        model = Player
        fields = ('url', 'uid', 'xp', 'level', 'trophies', 'powerups')
