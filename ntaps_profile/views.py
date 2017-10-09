from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
response = {'name': "Hash Slinging Slasher", 'birthday': "29 Feb", 'gender': "Unknown", 'description': "A dead Krusty Krab's cook", 'email': "hashslinging@krustykrab.bb"}
expertise = ["Rusty spatula", "Red eyes", "A cook", "Male", "Ghost", "Clumsy"]
def index(request):
    html = 'profile/ntaps_profile.html'
    response['expertise'] = expertise
    return render(request, html, response)
