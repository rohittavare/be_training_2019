#urls.py
from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

# URL prefix is '/prefix/'
urlpatterns = [
    url(r'^(?P<poke_slug>[^/]+)/$', views.handler, name='poo')
]
