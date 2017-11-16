from django.conf.urls import url

from . import views

urlpatterns = [ 
        url(r'^login$', views.login, name='login'),
        url(r'^confirm_login$', views.confirm_login, name='confirm_login'),
]
