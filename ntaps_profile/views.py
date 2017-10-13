from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile

# Create your views here.
#response = {'name': "Hash Slinging Slasher", 'birthday': "29 Feb", 'gender': "Unknown", 'description': "A dead Krusty Krab's cook", 'email': "hashslinging@krustykrab.bb"}
expertise = ["Rusty spatula", "Red eyes", "A cook", "Missing", "Ghost", "Clumsy"]
name = 'Hash Slinging Slasher'
birthday = '29 Feb'
gender = 'Unknown'
description = "A dead krusty krab's cook"
email = 'hashslinging@krustykrab.bb'
profile = Profile(name = 'Hash Slinging Slasher', birthday = '29 Feb', gender = 'Unknown', email = 'hashslinging@krustykrab.bb', description = "A dead krusty krab's cook", expertise = ["Rusty spatula", "Red eyes", "A cook", "Missing", "Ghost", "Clumsy"])
profile.save()
response = {}
def index(request):
    response['name'] = name
    response['birthday'] = birthday
    response['email'] = email
    response['description'] = description
    response['gender'] = gender
    response['expertise'] = expertise

    html = 'profile/ntaps_profile.html'

    return render(request, html, response)
