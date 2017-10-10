from django.http import HttpResponseRedirect
from .forms import Status_Form
from .models import Status
from django.shortcuts import render, redirect

# Create your views here.

status_dict ={}

response = {'author': "Ling In"} #TODO Implement yourname
def index(request):
    response['content'] = landing_page_content
    html = 'update_status/update_status.html'
    #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
    response['status_form'] = Status_Form

    status = Status.objects.all().order_by('-created_date')
    response['status'] = status
    return render(request, html, response)

def add_status(request):
	form = Status_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['status'] = request.POST['status']
		status = Status(status=response['status'])
		status.save()
		return redirect('/update_status/')
	else:
		return HttpResponseRedirect('/update_status/')