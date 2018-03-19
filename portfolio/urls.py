from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.abc, name='abc'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home2/$', views.home2, name='home2'),
    url(r'^volunteer/$', views.volunteer_list, name='volunteer_list'),
    url(r'^volunteer/(?P<pk>\d+)/delete/$', views.volunteer_delete, name='volunteer_delete'),
    url(r'^volunteer/(?P<pk>\d+)/edit/$', views.volunteer_edit, name='volunteer_edit'),
    url(r'^volunteer/create/$', views.volunteer_new, name='volunteer_new'),

    url(r'^inventory/$', views.inventory_list, name='inventory_list'),
    url(r'^inventory2/$', views.inventory_list2, name='inventory_list2'),
    url(r'^inventory/(?P<pk>\d+)/delete/$', views.inventory_delete, name='inventory_delete'),
    url(r'^inventory/(?P<pk>\d+)/edit/$', views.inventory_edit, name='inventory_edit'),
    url(r'^inventory/create/$', views.inventory_new, name='inventory_new'),

    url(r'^client/$', views.client_list, name='client_list'),
    url(r'^client2/$', views.client_list2, name='client_list2'),
    url(r'^client/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client/create/$', views.client_new, name='client_new'),
    ]
