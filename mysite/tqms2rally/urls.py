__author__ = 'Skye'

from django.conf.urls import patterns, url
from tqms2rally import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       )