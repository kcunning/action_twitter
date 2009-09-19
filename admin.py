from django.contrib import admin
from action_twitter.models import ActionItem, Tweet

class ActionItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ['title'] }
	
class TweetAdmin(admin.ModelAdmin):
	pass

admin.site.register(ActionItem, ActionItemAdmin)
admin.site.register(Tweet, TweetAdmin)