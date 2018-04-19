from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),                          
    url(r'^users$', views.index),                                       #GET route
    url(r'^users/new$', views.new),                                     #GET route
    url(r'^users/create$', views.create),                               #POST route
    url(r'^users/update/(?P<id>\d+)$', views.update),                               #POST route
    url(r'^users/(?P<id>\d+)/edit$', views.edit),                       #GET route
    url(r'^users/(?P<id>\d+)$', views.show),                            #GET route
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),                 #GET route

]
