from django.shortcuts import render
from django.http import HttpResponseRedirect
from ntaps_profile.models import Profile

# Create your views here.
#response = {'name': "Hash Slinging Slasher", 'birthday': "29 Feb", 'gender': "Unknown", 'description': "A dead Krusty Krab's cook", 'email': "hashslinging@krustykrab.bb"}
#expertise = ["Rusty spatula", "Red eyes", "A cook", "Unknown", "Ghost", "Clumsy"]
def index(request):
    profile = Profile.objects.first()

    #terus digimanain
    name = profile.name
    birthday = profile.birthday
    gender = profile.gender
    expertise = profile.expertise
    email = profile.email
    description = profile.description
    #picture_url ?

    html = 'profile/ntaps_profile.html'
    response['expertise'] = exp ertise
    return render(request, html, response)
