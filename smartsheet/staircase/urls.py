from django.conf.urls import url

from . import  views

urlpatterns=[
	url(r'^$',views.index,name='index'),
    url(r'^foups/$',views.foups,name='foups'),
    url(r'^foups/create$',views.create_foup,name='create_foup'),
    url(r'^foups/save_foup',views.save_foup,name='save_foup'),
    url(r'^foups/(?P<foup_name>F[0-9]+)/$',views.foup_detail,name='foup_detail'),
    url(r'^project/',views.project,name='project'),
    url(r'^split/',views.split,name='split'),
    url(r'^user/$',views.user,name='user'),
    url(r'^chamber/',views.chamber,name='chamber'),
    url(r'^measurementResult/',views.measurementResult,name='measurementResult'),
    url(r'^user/create/$',views.create_user,name='create_user'),
    url(r'^user/create/save_user',views.save_user,name='save_user'),
]