import logging

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites import requests
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime

from django.urls import reverse_lazy
from django.views import generic, View
import requests
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Service, Client, Doctor, Shedule, Doctor_Category

logger = logging.getLogger(__name__)
class HomeView(View):
    @staticmethod
    def get(request):

        response = requests.get('https://dog.ceo/api/breeds/image/random')
        image_url = response.json()['message']

        response = requests.get('https://www.boredapi.com/api/activity')
        act = response.json()['activity']

        context = {
            'image_url': image_url,
            'activity': act
        }

        return render(request, 'CosmetologyApp/index.html', context)



class UserProfileView(View):
    @staticmethod
    def get(request):
        try:
            doctor = Doctor.objects.get(username=request.user.username)
            # phone = Doctor.object.get(number=request.user.number)
        except Doctor.DoesNotExist:
            raise Http404('Client not found')

        return render(
            request,
            'CosmetologyApp/personal.html',
            context={'doctor' : doctor, })



class SheduleCreate(CreateView):

    model = Shedule
    fields = ['doctor', 'client', 'service', 'room', 'date']
    success_url = reverse_lazy('shedule')




class SheduleUpdate(UpdateView):
    model = Shedule
    fields = ['doctor', 'client', 'service', 'room', 'date']
    success_url = reverse_lazy('shedule')

class SheduleDetailsView(View):
    @staticmethod
    def get(request, id):
        try:
            shedule = Shedule.objects.get(id=id)
        except Shedule.DoesNotExist:
            raise Http404("Animal doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/shedule_detail.html',
            context={'shedule': shedule, }
        )
class SheduleDelete(DeleteView):
    model = Shedule
    success_url = reverse_lazy('shedule')

class DoctortForm(forms.Form):
    num_validetor = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")
    # validate_name = RegexValidator(regex=r"/^[a-z ,.'-]+$/i")
    name = forms.CharField(max_length=20)
    number = forms.CharField(max_length=30, validators=[num_validetor], help_text="+375 (29) xxx-xx-xx")
    password = forms.CharField()



def UserRegistration(request):
    if request.method == "POST":
        doctorForm = DoctortForm(request.POST)
        if doctorForm.is_valid():
            user = User()
            user.username = doctorForm.cleaned_data['name']
            user.password = make_password(doctorForm.cleaned_data['password'])
            user.save()
            request.user = user
            doctor = Doctor()
            doctor.name = user.username
            doctor.number = doctorForm.cleaned_data['number']
            doctor.save()
            logger.info(f'Registration new user {doctor.id}: {doctor.name}')
            return HttpResponseRedirect('/CosmetologyApp/accounts/login/')
        else:
            logger.error('Failed to registration user')
    else:
        doctorForm = DoctortForm()

    return render(
            request,
            'CosmetologyApp/registration.html',
            context={'form' : doctorForm, })





class ServiceListView(generic.ListView):
    model = Service
    context_object_name = 'service_list'
    template_name = 'CosmetologyApp/service.html'

class ClientListView(generic.ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = 'CosmetologyApp/client.html'

class DoctorListView(generic.ListView):
    model = Doctor
    context_object_name = 'doctor_list'
    template_name = 'CosmetologyApp/doctor.html'

class SheduleListView(generic.ListView):
    model = Shedule
    context_object_name = 'shedule_list'
    template_name = 'CosmetologyApp/shedule.html'

# class ClientDetailView(generic.DetailView):
#     model = Client
class ClientDetailView(View):
    def get(request, id):
        try:
            client_details = Client.objects.get(id=id)
        except Client.DoesNotExist:
            raise Http404("Placement doesn't exist :(")

        return render(
            request,
            'CosmetologyApp/client_detail.html',
            context={'client_details': client_details, }
        )


class DoctorDetailView(View):
    def get(request, id):
        try:
            doctor_details = Client.objects.get(id=id)
        except Client.DoesNotExist:
            raise Http404("Placement doesn't exist :(")

        return render(
            request,
            'CosmetologyApp/doctor_detail.html',
            context={'doctor_details': doctor_details, }
        )