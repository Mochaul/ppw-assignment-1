from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
response = {'author': "Hash Slinging Slasher"}
about_me = ["Rusty spatula", "Red eyes", "A cook", "Male", "Ghost", "Clumsy"]
def index(request):
    html = 'profile/ntaps_profile.html'
    response['about_me'] = about_me
    return render(request, html, response)
