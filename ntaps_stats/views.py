from django.shortcuts import render
from django.http import HttpResponseRedirect
from ntaps_add_friend.models import Friend
from ntaps_update_status.models import Status
from ntaps_profile.views import name

response = {}
def index(request):
    response['friend_total'] = Friend.objects.count()
    response['status_total'] = Status.objects.count()
    response['latest_status'] = Status.objects.last()
    response['name'] = name
    html = 'stats/ntaps_stats.html'
    return render(request, html, response)

# Create your views here.
