from django.conf.urls.defaults import patterns, include
from apps.jobs.views import *

urlpatterns = patterns('',
    (r'^$', main),
    (r'^post/$', post_job),

    (r'^tag/$', view_tag),

    (r'^search/', include('haystack.urls')),
)