from django.contrib.auth.models import User, Group
from django.contrib import admin
from peMuse.api.models import Player

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Player)