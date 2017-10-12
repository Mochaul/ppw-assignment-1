from django.shortcuts import render
from django.http import HttpResponseRedirect

response = {'name': "Hash Slinging Slasher",'friends' : "120 people", 'feed' : "23 Post"}
def index(request):
    html = 'stats/ntaps_stats.html'
    return render(request, html, response)

# Create your views here.
