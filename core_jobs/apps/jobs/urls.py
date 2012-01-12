from django.conf.urls.defaults import patterns, include
from apps.jobs.views import *

# Tastypie API
from tastypie.api import Api
from apps.jobs.api import *
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())

urlpatterns = patterns('',
    (r'^$', main),
    (r'^post/$', post_job),

    (r'^tag/$', view_tag),

    (r'^search/', include('haystack.urls')),

    (r'^api/', include(v1_api.urls)),
)