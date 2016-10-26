from django.conf.urls import url


from sbleague import views

urlpatterns = [
# url/
    url('^$', views.index, name='index'),
    url(r'^team/(?P<team_id>\d+)/(?P<order>\w+)$',views.team ),
    url(r'^team/(?P<team_id>\d+)/',views.team ),
    url(r'^team/(?P<pos>\w+)/(?P<order>\w+)$',views.allteam ),
    url(r'^people/(?P<member_id>\d+)/$',views.people ),
    url(r'^newgame$',views.newgame,name='newgame'),
    url(r'^batting/(?P<order>\w+)/$',views.allbatting ),
    url(r'^pitching/(?P<order>\w+)/$',views.allpitching ),
    url(r'^game/(?P<game_id>\d+)/$',views.game),
    url(r'^game$',views.allgame),
    url(r'^addgame/$',views.addgame,name='addgame'),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^mod/(?P<game_id>\d+)$',views.mod),
    url(r'^register$',views.register,name="register"),
    url(r'^nowplayer$',views.nowplayer,name="nowplayer"),
    url(r'^clear_register$',views.clear_register,name="clear_register")
]