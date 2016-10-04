from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, renderers
from peMuse.api import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)

router.register(r'trophies', views.TrophyViewSet)
router.register(r'powerups', views.PowerupViewSet)
router.register(r'player-powerups', views.PlayerPowerupViewSet)
router.register(r'player-trophies', views.PlayerTrophyViewSet)

player_add_xp = views.PlayerViewSet.as_view({
    'get': 'add_xp' #TODO make this a post instead of get to be more RESTful..
}, renderer_classes=[renderers.StaticHTMLRenderer])

player_set_xp = views.PlayerViewSet.as_view({
    'get': 'set_xp' #TODO make this a post instead of get to be more RESTful..
}, renderer_classes=[renderers.StaticHTMLRenderer])

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^players/(?P<pk>\d+)/add_xp/(?P<xp>\d+)/$', player_add_xp, name='player-add-xp'),
    url(r'^players/(?P<pk>\d+)/set_xp/(?P<xp>\d+)/$', player_set_xp, name='player-set-xp'),

    # Additionally, we include login URLs for the browsable API and admin
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),  # And admin panel
]
