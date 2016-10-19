from rest_framework import serializers
from peMuse.api.models import Player, Powerup, PlayerPowerup, Trophy, PlayerTrophy, Badge, Question, Terminal, \
    PlayerQuestion


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('url', 'id', 'uid', 'updated_at', 'active_player')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class TerminalSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)

    class Meta:
        model = Terminal


class PowerupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Powerup


class PlayerPowerupSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='powerup.name')  # Accessing the model
    icon_url = serializers.ReadOnlyField(source='powerup.icon_url')  # Accessing the model
    description = serializers.ReadOnlyField(source='powerup.description')

    class Meta:
        model = PlayerPowerup
        fields = ('name', 'description', 'quantity', 'icon_url', 'id')


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
    name = serializers.ReadOnlyField()
    icon_filename = serializers.ReadOnlyField()

    class Meta:
        model = Player
        fields = ('name', 'id', 'icon_filename', 'xp', 'level', 'url', 'trophies', 'powerups', 'played_with')


class PlayerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerQuestion
