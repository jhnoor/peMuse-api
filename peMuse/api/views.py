from rest_framework import viewsets
from serializers import PlayerSerializer, TrophySerializer, PowerupSerializer, PlayerPowerupSerializer, PlayerTrophySerializer
from peMuse.api.models import Player, PlayerPowerup, Powerup, Trophy, PlayerTrophy


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by("created_at")
    serializer_class = PlayerSerializer
    lookup_field = 'uid'


class TrophyViewSet(viewsets.ModelViewSet):
    """
        #Trophy list

        This lists all the trophies in the game. Users shall have all trophies in an intermediate table
        and an extra field "earned" that is default false

    """
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer
    lookup_field = 'name'


class PlayerTrophyViewSet(viewsets.ModelViewSet):
    """
        # Intermediate table Player-Trophy

        Each players trophies and whether they have earned them or not are stored here.
    """
    queryset = PlayerTrophy.objects.all()
    serializer_class = PlayerTrophySerializer


class PowerupViewSet(viewsets.ModelViewSet):
    """
        #Powerup list

        This lists all the powerups in the game. Users shall have all powerups in an intermediate table
        and an extra field "quantity" that is default 0

    """
    queryset = Powerup.objects.all().order_by("name")
    serializer_class = PowerupSerializer
    lookup_field = 'name'


class PlayerPowerupViewSet(viewsets.ModelViewSet):
    """
        # Intermediate table Player-Powerups

        Each players powerups and quantity is listed here.
    """
    queryset = PlayerPowerup.objects.all()
    serializer_class = PlayerPowerupSerializer
