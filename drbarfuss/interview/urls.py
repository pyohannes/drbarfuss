from django.conf.urls import url

from . import views

urlpatterns = [ 
        url(r'^ask/(?P<runkey>\w+)/(?P<index>\d+)$', views.ask, name='ask'),
        url(r'^evaluate/(?P<runkey>\w+)$', views.evaluate, name='evaluate'),
]
