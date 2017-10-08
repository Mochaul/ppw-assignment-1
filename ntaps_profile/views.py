from django.shortcuts import render
from lab_2.views import landing_page_content
from django.http import HttpResponseRedirect

# Create your views here.
response = {'author': "Hash Slinging Slasher"}
about_me = ["Rusty spatula", "Red eyes", "A cook", "Male", "Ghost", "Clumsy"]
def index(request):
    response['content'] = landing_page_content
    html = 'ntaps_profile/profile.html'
    response['about_me'] = about_me
    return render(request, html, response)
