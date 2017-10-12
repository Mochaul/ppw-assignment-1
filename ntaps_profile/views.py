from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.
response = {'name': "Hash Slinging Slasher", 'birthday': "29 Feb", 'gender': "Unknown", 'description': "A dead Krusty Krab's cook", 'email': "hashslinging@krustykrab.bb"}
expertise = ["Rusty spatula", "Red eyes", "A cook", "Missing", "Ghost", "Clumsy"]
def index(request):

    #terus digimanain
    name = Profile.name
    birthday = Profile.birthday
    gender = Profile.gender
    expertise = Profile.expertise
    email = Profile.email
    description = Profile.description

    html = 'profile/ntaps_profile.html'
    response['expertise'] = expertise
    return render(request, html, response)
