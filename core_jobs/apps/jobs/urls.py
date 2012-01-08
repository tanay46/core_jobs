from django.conf.urls.defaults import patterns, include, url
from apps.jobs.views import *

urlpatterns = patterns('',
    (r'^$', main),
    (r'^post/$', post_job),
    (r'^tag/$', view_tag),
)