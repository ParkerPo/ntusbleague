from django.conf.urls import url


from sbleague import views

urlpatterns = [
# url/
    url('^$', views.index, name='index'),
    url(r'^team/(?P<team_id>\d+)/$',views.team , name='thatteam'),
    url(r'^team$',views.allteam , name='allteam'),
    url(r'^people/(?P<member_id>\d+)/$',views.people , name='thatpeople'),
    url(r'^newgame$',views.newgame,name='newgame'),
    url(r'^batting/(?P<order>\w+)/$',views.allbatting , name='allbatting'),
    url(r'^pitching/(?P<order>\w+)/$',views.allpitching , name='allpitching'),
    url(r'^game/(?P<game_id>\d+)/$',views.game,name='game'),
    url(r'^game$',views.allgame, name='allgame'),
    url(r'^addgame/$',views.game,name='addgame'),
    url(r'^login$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^mod/(?P<game_id>\d+)$',views.mod,name='mod'),
    
]