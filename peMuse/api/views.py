from rest_framework import viewsets, renderers, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from serializers import PlayerSerializer, TrophySerializer, PowerupSerializer, PlayerPowerupSerializer, \
    PlayerTrophySerializer, BadgeSerializer, TerminalSerializer, QuestionSerializer
from peMuse.api.models import Player, PlayerPowerup, Powerup, Trophy, PlayerTrophy, Badge, Terminal, Question


## Viewsets ##

class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all().order_by("-updated_at")
    serializer_class = BadgeSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer], methods=['post'])
    def new_active_player(self, *args, **kwargs):
        if 'pk' not in kwargs:
            raise TypeError("new_active_player requires pk parameter e.g. 'players/<pk>'")
        new_player = Player.objects.create()
        badge = Badge.objects.get(pk=kwargs['pk'])
        if badge.active_player is not None:
            return Response({"badge unavailable, assigned to " + str(badge.active_player)},
                            status=status.HTTP_412_PRECONDITION_FAILED)
        badge.active_player = new_player
        badge.save()
        return Response({new_player.pk}, status=status.HTTP_200_OK)


class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer], methods=['put'])
    def set_online(self, *args, **kwargs):
        terminal = self.get_object()
        if terminal.set_online():
            terminal.save()
            return Response(data=terminal.pk, status=status.HTTP_200_OK)
        else:
            return Response({"terminal already online"}, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer], methods=['put'])
    def set_offline(self, *args, **kwargs):
        terminal = self.get_object()
        if terminal.set_offline():
            terminal.save()
            return Response(data=terminal.pk, status=status.HTTP_200_OK)
        else:
            return Response({"terminal already offline"}, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by("created_at")
    serializer_class = PlayerSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def add_xp(self, *args, **kwargs):
        player = self.get_object()
        player.add_xp(**kwargs)
        return Response({"add_xp success": "player_" + str(player.pk) + " got xp!"}, status=status.HTTP_200_OK)

    def set_xp(self, *args, **kwargs):
        if 'xp' not in kwargs:
            raise TypeError("set_xp requires xp parameter e.g. 'players/<pk>/<xp>'")
        player = self.get_object()
        player.set_xp(kwargs['xp'])
        return Response({"set_xp success"}, status=status.HTTP_200_OK)

    def set_powerup_quantity(self, *args, **kwargs):
        if 'powerup_pk' not in kwargs:
            raise TypeError("set_powerup_quantity requires powerup_pk parameter e.g. 'players/<pk>/<powerup_pk>'")
        if 'quantity' not in kwargs:
            raise TypeError("quantity parameter required e.g. 'players/<pk>/<powerup_pk>/<quantity>'")
        player = self.get_object()
        player.set_powerup_quantity(kwargs['powerup_pk'], kwargs['quantity'])
        return Response({"set_powerup_quantity success"}, status=status.HTTP_200_OK)

    def earn_trophy(self, *args, **kwargs):
        if 'trophy_pk' not in kwargs:
            raise TypeError("earn_trophy requires trophy_pk parameter e.g. 'players/<pk>/<trophy_pk>'")
        player = self.get_object()
        player.earn_trophy(kwargs['trophy_pk'])
        return Response({"earn_trophy success"}, status=status.HTTP_200_OK)


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


class PlayerPowerupViewSet(viewsets.ModelViewSet):
    """
        # Intermediate table Player-Powerups

        Each players powerups and quantity is listed here.
    """
    queryset = PlayerPowerup.objects.all()
    serializer_class = PlayerPowerupSerializer
