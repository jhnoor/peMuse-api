from rest_framework import viewsets
from serializers import PlayerSerializer, TrophySerializer, PowerupSerializer
from peMuse.api.models import Player, PlayerPowerup, Powerup, Trophy


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TrophyViewSet(viewsets.ModelViewSet):
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer


class PowerupViewSet(viewsets.ModelViewSet):
    queryset = Powerup.objects.all()
    serializer_class = PowerupSerializer

