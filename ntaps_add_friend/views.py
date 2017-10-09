from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Friend
from .forms import Add_Friend_Form

# Create your views here.
response = {}
def index(request):
    html = 'add_friend/ntaps_add_friend.html'
    response['friends'] = Friend.objects.all()
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
