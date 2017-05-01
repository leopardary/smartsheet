from django.conf.urls import url

from . import  views

urlpatterns=[
	url(r'^$',views.index,name='index'),
    url(r'^foups/',views.foups,name='foups'),
    url(r'^project/',views.project,name='project'),
    url(r'^split/',views.split,name='split'),
    url(r'^user/$',views.user,name='user'),
    url(r'^chamber/',views.chamber,name='chamber'),
    url(r'^measurementResult/',views.measurementResult,name='measurementResult'),
    url(r'^user/create',views.create_user,name='create_user'),
]