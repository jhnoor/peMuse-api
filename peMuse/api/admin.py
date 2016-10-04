from django.contrib.auth.models import User, Group
from django.contrib import admin
from peMuse.api.models import Player, Trophy, Powerup, PlayerPowerup, PlayerTrophy
from peMuse.api.models import Terminal, Session, Badge

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

# Player
admin.site.register(Player)
admin.site.register(Powerup)
admin.site.register(Trophy)
# admin.site.register(PlayerPowerup)
# admin.site.register(PlayerTrophy)

# Terminal
admin.site.register(Terminal)
admin.site.register(Session)
admin.site.register(Badge)
