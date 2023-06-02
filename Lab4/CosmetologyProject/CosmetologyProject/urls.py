"""CosmetologyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path, include

# import CosmetologyApp.views

urlpatterns = [
    # re_path(r'^$', CosmetologyApp.views.index, name='index'),
    # re_path(r'^home$', CosmetologyApp.views.index, name='home'),
    # re_path(r'^about$', CosmetologyApp.views.about, name='about'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('CosmetologyApp/')),
    path('CosmetologyApp/', include('CosmetologyApp.urls'))

]
