from django.conf.urls import url
from .views import index, create
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'create/', create, name='create'),
]
