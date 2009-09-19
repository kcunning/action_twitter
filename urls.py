from django.conf.urls.defaults import *

# These are sample URL patterns for you! Chances are, you'll want to splice this app up how you need.

urlpatterns = patterns('',
	(r'^action_items/$', 'action_twitter.views.action_items'),
)