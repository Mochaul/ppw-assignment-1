from django.http import HttpResponseRedirect
from .forms import Status_Form, Comment_Form
from .models import Status, Comment
from django.shortcuts import render, redirect, get_object_or_404
from ntaps_profile.models import Profile

# Create your views here.

status_dict ={}

response = {'author': "Ling In"} #TODO Implement yourname
def index(request):
    html = 'update_status/update_status.html'
    #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
    response['status_form'] = Status_Form
    response['comment_form'] = Comment_Form
    response['profile'] = Profile
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

def add_comment(request, pk):
	status = Status.objects.get(pk=pk)
	form = Comment_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['comment'] = request.POST['comment']
		comment=Comment(comment=response['comment'])
		comment.status = status
		comment.save()
		return redirect('/update_status/')
	else:
		return HttpResponseRedirect('/update_status/')

def delete_status(request, object_id):
	status = Status.objects.get(pk=object_id)
	status.delete()
	return HttpResponseRedirect('/update_status/')
