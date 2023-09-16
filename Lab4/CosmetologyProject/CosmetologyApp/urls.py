from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.urls import re_path

from . import views
# from views import index

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/accounts/login/CosmetologyApp/accounts/', include('django.contrib.auth.urls')),
    re_path(r'^registration/$', views.UserRegistration, name='registration'),
    path('service/', views.ServiceListView.as_view(), name='service'),
    path('service/<int:id>/', views.ServiceDetailsView.as_view(), name='detail_service'),
    path('service/add/', views.ServiceCreate.as_view(), name='add_service'),
    path('service/<int:pk>/delete/', views.ServiceDelete.as_view(), name='delete_service'),

    path('shedule/', views.SheduleListView.as_view(), name='shedule'),
    path('shedule/<int:id>/', views.SheduleDetailsView.as_view(), name='detail_shedule'),
    path('shedule/add/', views.SheduleCreate.as_view(), name='add_shedule'),
    path('shedule/<int:pk>/edit/', views.SheduleUpdate.as_view(), name='edit_shedule'),
    path('shedule/<int:pk>/delete/', views.SheduleDelete.as_view(), name='delete_shedule'),


    path('client/', views.ClientListView.as_view(), name='client'),
    path('client/<int:pk>/', views.ClientDetailsView.as_view(), name='detail_client'),
    path('client/add/', views.ClientCreate.as_view(), name='add_client'),
    path('client/<int:pk>/edit/', views.ClientUpdate.as_view(), name='edit_client'),
    path('client/<int:pk>/delete/', views.ClientDelete.as_view(), name='delete_client'),

    path('promocode/', views.PromocodeView.as_view(), name='promocode'),
    path('promocode/<int:id>/', views.PromocodeDetailsView.as_view(), name='detail_promocode'),
    path('promocode/add/', views.PromocodeCreate.as_view(), name='add_promocode'),
    path('promocode/<int:pk>/delete/', views.PromocodeDelete.as_view(), name='delete_promocode'),

    path('doctor/', views.DoctorListView.as_view(), name='doctor'),
    path('doctor/<int:id>/', views.DoctorDetailView.as_view(), name='detail_doctor'),

    # path(r'^doctor$', views.DoctorListView.as_view(), name='doctor'),
    # path(r'doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),

    path('diagram/', views.DiagramView.as_view(), name='diagram'),
    path('static_info/', views.StaticInfoView.as_view(), name='static_info'),
    path('about_company/', views.AboutCompanyInfoView.as_view(), name='about_company'),
    path('news/', views.News.as_view(), name='news'),
    path('ancient_cosmetic/', views.ancient_cosmetic.as_view(), name='ancient_cosmetic'),
    path('injectable_procedures/', views.injectable_procedures.as_view(), name='injectable_procedures'),
    path('Influence_of_technology/', views.Influence_of_technology.as_view(), name='Influence_of_technology'),
    path('Mens_grooming/', views.Mens_grooming.as_view(), name='Mens_grooming'),
    path('faq/', views.faq.as_view(), name='faq'),
    path('private_policy/', views.private_policy.as_view(), name='private_policy'),
    path('vacancy/', views.vacancy_View.as_view(), name='vacancy'),
    path('vacancy/<int:id>/', views.VacancyDetailsView.as_view(), name='detail_vacancy'),
    path('vacancy/add/', views.VacancyCreate.as_view(), name='add_vacancy'),
    path('vacancy/<int:pk>/delete/', views.VacancyDelete.as_view(), name='delete_vacancy'),
    path('rewiew/', views.rewiew.as_view(), name='rewiew'),
    path('rewiew/add/', views.RewiewCreate, name='add_rewiew'),



]

