from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from . import views
# from views import index

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^registration/$', views.UserRegistration, name='registration'),
    re_path('personal/', views.UserProfileView.as_view(), name='user'),
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('shedule/', views.SheduleListView.as_view(), name='shedule'),
    path('client/', views.ClientListView.as_view(), name='client'),
    re_path(r'^personal/$', views.UserProfileView.as_view(), name='user'),
    path(r'^doctor$', views.DoctorListView.as_view(), name='doctor'),
    path(r'client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    path(r'doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),


]

