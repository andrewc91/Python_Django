from django.conf.urls import url
from . import views

# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^usercourse', views.usercourse, name='usercourse')
]
