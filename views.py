from django.shortcuts import get_object_or_404, render_to_response
from action_twitter.models import ActionItem, Tweet

def action_item(request, slug):
	action_item = get_object_or_404(ActionItem,
                slug = slug)
	tweets = Tweet.objects.filter(tweet__icontains=slug)
	print tweets
	
	return render_to_response('action_twitter/action_item.html',
							{'action_item': action_item,
							'tweets': tweets})


def action_items(request):
	return render_to_response('action_twitter/action_items.html',
							{'action_items': ActionItem.objects.all()}	)