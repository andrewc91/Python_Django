from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^users_courses$', views.users_courses, name='users_courses'),
    url(r'^assign$', views.assign, name='assign')
]
