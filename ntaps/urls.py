"""ntaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
import ntaps_profile.urls as ntaps_profile
import ntaps_add_friend.urls as ntaps_add_friend
import ntaps_update_status.urls as ntaps_update_status
import ntaps_stats.urls as ntaps_stats

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include(ntaps_profile,namespace='profile')),
    url(r'^add_friend/', include(ntaps_add_friend,namespace='add_friend')),
    url(r'^update_status/', include(ntaps_update_status,namespace='update_status')),
    url(r'^stats/', include(ntaps_stats,namespace='stats')),
    url(r'^$', RedirectView.as_view(permanent=True, url='/update_status/'))
]
