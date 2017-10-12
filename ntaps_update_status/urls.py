from .views import index, add_status, add_comment, delete_status
from django.conf.urls import url

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_status', add_status, name='add_status'),
	#url(r'^add_comment', add_comment, name='add_comment'),
	#url(r'^add_comment/(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
	url(r'^add_comment/(?P<pk>[0-9]+)/$', add_comment, name='add_comment'),
	url(r'^delete_status/(?P<object_id>[0-9]+)',delete_status,name='delete_status'),
	#url(r'^delete_status', delete_status, name='delete_status'),
]
