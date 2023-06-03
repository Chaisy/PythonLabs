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
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('shedule/', views.SheduleListView.as_view(), name='shedule'),
    path('shedule/<int:pk>/delete/', views.SheduleDelete.as_view(), name='delete_shedule'),
    path('shedule/<int:pk>/edit/', views.SheduleUpdate.as_view(), name='edit_shedule'),
    path('shedule/<int:id>/', views.SheduleDetailsView.as_view(), name='animal'),
    path('client/', views.ClientListView.as_view(), name='client'),
    path(r'^doctor$', views.DoctorListView.as_view(), name='doctor'),
    path(r'client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    path(r'doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('shedule/add/', views.SheduleCreate.as_view(), name='add_shedule'),


]

