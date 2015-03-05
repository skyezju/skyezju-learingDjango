__author__ = 'Skye'

from django.conf.urls import patterns, url
from upload import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       #url(r'^(?P<pk>\d+)/$', views.UploadFromFileView.as_view(), name='uploadfromfile'),
                       url(r'1/$', views.upload),
                       url(r'2/$', views.upload_file),
                       #url(r'1/$', views.UploadFromTextView.as_view(), name='uploadfromtext'),
                       )