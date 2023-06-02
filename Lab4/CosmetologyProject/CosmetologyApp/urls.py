
from django.urls import path
from django.urls import re_path

from . import views
# from views import index

urlpatterns = [

    path('', views.index),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home$', views.index, name='home'),
    # re_path(r'^service$', views.service, name='service'),
    path(r'^service$', views.ServiceListView.as_view(), name='service'),
    path(r'^shedule$', views.SheduleListView.as_view(), name='shedule'),
    path(r'^client$', views.ClientListView.as_view(), name='client'),
    path(r'^doctor$', views.DoctorListView.as_view(), name='doctor'),
    # url(r'^client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    path(r'client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    path(r'doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),
    # path('', views.index)
    # re_path(r'^$', views.index, name='index'),
    # re_path(r'^animals/$', views.animals, name='animals'),
    # re_path(r'^placements/$', views.placements, name='placements'),

]

# urlpatterns = [
    # re_path(r'^$', CosmetologyApp.views.index, name='index'),
    # re_path(r'^home$', CosmetologyApp.views.index, name='home'),
    # re_path(r'^about$', CosmetologyApp.views.about, name='about'),
