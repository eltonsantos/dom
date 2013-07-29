from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('launch.urls', namespace="launch", app_name="launch")),
    url(r'^admin/', include(admin.site.urls)),
)
