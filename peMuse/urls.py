from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, renderers
from peMuse.api import views

from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'trophies', views.TrophyViewSet)
router.register(r'powerups', views.PowerupViewSet)
router.register(r'player-powerups', views.PlayerPowerupViewSet)
router.register(r'player-trophies', views.PlayerTrophyViewSet)
router.register(r'badges', views.BadgeViewSet)
router.register(r'terminals', views.TerminalViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'player-questions', views.PlayerQuestionViewSet)


player_add_xp = views.PlayerViewSet.as_view({
    'put': 'add_xp'
}, renderer_classes=[renderers.StaticHTMLRenderer])

player_update_player = views.PlayerViewSet.as_view({
    'put': 'update_player'
}, renderer_classes=[renderers.StaticHTMLRenderer])

player_set_xp = views.PlayerViewSet.as_view({
    'put': 'set_xp'
}, renderer_classes=[renderers.StaticHTMLRenderer])

player_set_powerup_quantity = views.PlayerViewSet.as_view({
    'put': 'set_powerup_quantity'
}, renderer_classes=[renderers.StaticHTMLRenderer])

player_earn_trophy = views.PlayerViewSet.as_view({
    'put': 'earn_trophy'
}, renderer_classes=[renderers.StaticHTMLRenderer])

badge_new_active_player = views.BadgeViewSet.as_view({
    'post': 'new_active_player' # TODO why doesnt this work on post?
}, renderer_classes=[renderers.StaticHTMLRenderer])

terminal_set_online = views.TerminalViewSet.as_view({
    'put': 'set_online' # TODO why doesnt this work on post?
}, renderer_classes=[renderers.StaticHTMLRenderer])

terminal_set_offline = views.TerminalViewSet.as_view({
    'put': 'set_offline' # TODO why doesnt this work on post?
}, renderer_classes=[renderers.StaticHTMLRenderer])

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),

    # Players TODO instead of pk, use more accurate player_pk, badge_pk etc
    url(r'^players/(?P<pk>\d+)/add_xp/(?P<xp>\d+)/$', player_add_xp, name='player-add-xp'),
    url(r'^players/(?P<pk>\d+)/update_player/$', player_update_player, name='player-update-player'),
    url(r'^players/(?P<pk>\d+)/set_xp/(?P<xp>\d+)/$', player_set_xp, name='player-set-xp'),
    url(r'^players/(?P<pk>\d+)/set_powerup_quantity/(?P<powerup_pk>\d+)/(?P<quantity>\d+)/$',
        player_set_powerup_quantity, name='player-set-powerup-quantity'),
    url(r'^players/(?P<pk>\d+)/earn_trophy/(?P<trophy_pk>\d+)/$', player_earn_trophy, name='player-earn-trophy'),

    # Badges
    url(r'^badges/(?P<badge_pk>\d+)/new_active_player/$', badge_new_active_player, name='badge-new-active-player'),
    # Terminal
    url(r'^terminals/(?P<terminal_pk>\d+)/set_online/$', terminal_set_online, name='terminal-set-online'),
    url(r'^terminals/(?P<terminal_pk>\d+)/set_offline/$', terminal_set_offline, name='terminal-set-offline'),

    # Additionally, we include login URLs for the browsable API and admin
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),  # And admin panel

]
