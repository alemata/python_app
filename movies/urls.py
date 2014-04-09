from django.conf.urls import patterns, url

from movies import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^watchlist/$', views.watchlist, name='watchlist'),
                       url(r'^movie/(?P<movie_id>\d+)/$', views.movie_show, name='add_rating_to_movie'),
                       url(r'^movie/(?P<movie_id>\d+)/edit/$', views.movie_edit, name='add_rating_to_movie'),
                       url(r'^movie/(?P<movie_id>\d+)/add_rating$', views.add_rating_to_movie, name='add_rating_to_movie'),
                       url(r'^(?P<user_id>\d+)/mywatchlist/$', views.user_watchlist, name='user_watchlist'),
                       url(r'^movie/(?P<movie_id>\d+)/addtolist/$', views.add_movie_to_watchlist, name='add_movie_to_list'),
)
