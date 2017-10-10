from .views import index, add_status
from django.conf.urls import url

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_status', add_status, name='add_status')
]
