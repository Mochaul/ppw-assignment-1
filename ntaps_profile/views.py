from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.
expertise = ["Rusty spatula", "Red eyes", "A cook", "Missing", "Ghost", "Clumsy"]
name = 'Hash Slinging Slasher'
birthday = '29 Feb'
gender = 'Unknown'
description = "A dead krusty krab's cook"
email = 'hashslinging@krustykrab.bb'

response = {}
def index(request):
    profile = Profile(name = name, birthday = birthday, gender = gender, email = email, description = description, expertise = expertise)
    response = {'name': profile.name, 'birthday': profile.birthday, 'gender': profile.gender, 'description': profile.description, 'email': profile.email, 'expertise': profile.expertise}

    html = 'profile/ntaps_profile.html'

    return render(request, html, response)
