from django.conf.urls import url

from . import  views

urlpatterns=[
	url(r'^$',views.index,name='index'),
    url(r'^foups/$',views.foups,name='foups'),
    url(r'^foups/create$',views.create_foup,name='create_foup'),
    url(r'^foups/create/save_foup$',views.save_foup,name='save_foup'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/$',views.foup_detail,name='foup_detail'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/reclaim$',views.reclaim_wafers,name='reclaim_wafers'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/load$',views.load_wafers,name='load_wafers'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/load/execute$',views.load_execute,name='load_execute'),
    url(r'^project/',views.project,name='project'),
    url(r'^split/',views.split,name='split'),
    url(r'^user/$',views.user,name='user'),
    url(r'^chamber/',views.chamber,name='chamber'),
    url(r'^measurementResult/',views.measurementResult,name='measurementResult'),
    url(r'^user/create/$',views.create_user,name='create_user'),
    url(r'^user/create/save_user',views.save_user,name='save_user'),
]