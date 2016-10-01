from rest_framework import viewsets
from serializers import PlayerSerializer, TrophySerializer, PowerupSerializer
from peMuse.api.models import Player, PlayerPowerup, Powerup, Trophy


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by("created_at")
    serializer_class = PlayerSerializer


class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer


class PowerupViewSet(viewsets.ModelViewSet):
    queryset = Powerup.objects.all().order_by("name")
    serializer_class = PowerupSerializer
