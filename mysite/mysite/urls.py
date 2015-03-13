from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('upload.urls', namespace="upload")),
    (r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'./upload/static/upload/images'}),

)
