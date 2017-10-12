from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from urllib import request
from .models import Friend
from .forms import Add_Friend_Form

# Create your views here.
response = {}
def index(request):
    html = 'add_friend/ntaps_add_friend.html'
    response['offset'] = int(request.GET.get('offset', '0'))
    response['next_offset'] = response['offset'] + 5;
    response['prev_offset'] = response['offset'] - 5;
    response['disable_next'] = True if response['next_offset'] > Friend.objects.all().count() else False;
    response['disable_prev'] = True if response['prev_offset'] < 0 else False;
    start = response['offset']
    finish = response['offset'] + 5;
    response['friends'] = Friend.objects.all().order_by('-created_at')[start:finish]
    response['add_friend_form'] = Add_Friend_Form

    return render(request, html, response)

def create(request):
    form = Add_Friend_Form(request.POST or None)
    if (request.method == 'POST' and form.is_valid()):
        if (check_url(append_http(request.POST['url']))):
            response['name'] = request.POST['name']
            response['url'] = append_http(request.POST['url'])
            friend = Friend(name=response['name'], url=response['url'])
            friend.save()
            return HttpResponseRedirect('/add_friend/')
        else:
            messages.error(request, 'Url temanmu tidak bisa diakses. Format URL: http://ntaps.herokuapp.com')
            return HttpResponseRedirect('/add_friend/')
    else:
        for error, error_messages in form.errors.items():
            for message in error_messages:
                messages.error(request, message)
        return HttpResponseRedirect('/add_friend/')

def append_http(url):
    if((url[:7] != "http://") and (url[:8] != "https://")):
        return "http://{}".format(url)
    else:
        return url
def check_url(url):
    try:
        code = request.urlopen(url).getcode()
        return True
    except:
        return False;
