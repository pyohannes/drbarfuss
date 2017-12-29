from django.conf.urls import url

from . import views

urlpatterns = [ 
        url(r'^login$', views.login, name='login'),
        url(r'^logout$', views.logout, name='logout'),
        url(r'^overview$', views.overview, name='overview'),
        url(r'^order$', views.order, name='order'),
        url(r'^deleterun/(?P<runid>\d+)$', views.deleterun, name='deleterun'),
]
