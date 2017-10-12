from django.shortcuts import render
from django.http import HttpResponseRedirect

response = {'name': "Hash Slinging Slasher",'friends' : "666 people", 'feed' : "69(LOL) Post"}
def index(request):
    html = 'stats/ntaps_stats.html'
    return render(request, html, response)

# Create your views here.
