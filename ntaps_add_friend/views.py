from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name']
        response['url'] = request.POST['url']
        friend = Friend(name=response['name'], url=response['url'])
        friend.save()
        return HttpResponseRedirect('/add_friend/')
    else:
        return HttpResponseRedirect('/add_friend/')
