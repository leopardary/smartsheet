from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$', views.old_views.index, name='index'),
    url(r'^foups/$', views.foup_wafer.foups, name='foups'),
    url(r'^foups/create$', views.foup_wafer.create_foup, name='create_foup'),
    url(r'^foups/create/save_foup$', views.foup_wafer.save_foup, name='save_foup'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/$', views.foup_wafer.foup_detail, name='foup_detail'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/reclaim$', views.foup_wafer.reclaim_wafers, name='reclaim_wafers'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/reclaim/execute$', views.foup_wafer.reclaim_execute, name='reclaim_execute'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/load$', views.foup_wafer.load_wafers, name='load_wafers'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/load/execute$', views.foup_wafer.load_execute, name='load_execute'),
    url(r'^project/', views.old_views.project, name='project'),
    url(r'^split/', views.old_views.split, name='split'),
    url(r'^user/$', views.user, name='user'),   #when the module name is the same as the .py file name, the file name level is omitted. same as chamber below.
    url(r'^chamber/$', views.chamber, name='chamber'),
    url(r'^chamber/create/$', views.create_chamber, name='create_chamber'),
    url(r'^chamber/create/save_chamber$', views.save_chamber, name='save_chamber'),
    url(r'^chamber/(?P<chamber_id>[0-9]+)$', views.chamber_detail, name='chamber_detail'),
    #url(r'^chamber/(?P<chamber_id>[0-9]+)/update$',views.chamber_update,name='chamber_update'),
    url(r'^chamber/(?P<chamber_id>[0-9]+)/delete$', views.chamber_delete, name='chamber_delete'),
    url(r'^measurementResult/', views.old_views.measurementResult, name='measurementResult'),
    url(r'^user/create/$', views.create_user, name='create_user'),
    url(r'^user/create/save_user', views.save_user, name='save_user'),
    url(r'^recipe/$', views.recipe, name='processrecipe'),
    url(r'^recipe/create/$', views.create_recipe, name='create_recipe'),
    url(r'^thickness/$', views.old_views.thickness, name='thickness'),

]