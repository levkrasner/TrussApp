from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getname/', views.getName, name='getName'),
    url(r'^getInput/', views.getInput, name='getInput'),
    url(r'^savetenant/', views.save_tenant, name='save_tenant'),
    url(r'^getallTenants/', views.get_all_tenants, name='get_all_tenants'),
    url(r'^first/', views.get_first_request, name='get_first_request'),


]