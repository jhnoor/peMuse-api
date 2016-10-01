from rest_framework import viewsets
from serializers import PlayerSerializer
from peMuse.api.models import Player, PlayerPowerups, Powerup, Trophy


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer



"""
class GroupViewSet(viewsets.ModelViewSet):

    # API endpoint that allows groups to be viewed or edited.

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""
