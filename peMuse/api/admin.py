from django.contrib.auth.models import User, Group
from django.contrib import admin
from peMuse.api.models import Player, Trophy, Powerup, PlayerPowerup

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Player)
admin.site.register(Powerup)
admin.site.register(Trophy)
admin.site.register(PlayerPowerup)