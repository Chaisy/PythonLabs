import logging
import re

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites import requests
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.utils.decorators import method_decorator
from plotly.graph_objects import Bar, Layout, Figure
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime

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
            context={'doctor': doctor, })


# Client#########################
@method_decorator(login_required, name='dispatch')
class ClientDetailsView(View):
    @staticmethod
    def get(request, id):
        try:
            client = Client.objects.get(id=id)
        except Client.DoesNotExist:
            raise Http404("client doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/client_detail.html',
            context={'client': client, }
        )


@method_decorator(login_required, name='dispatch')
class ClientCreate(CreateView):
    model = Client
    fields = ['name', 'number', 'birth_date']
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Client.objects.filter(name=form.cleaned_data['name']) and \
                Client.objects.filter(number=form.cleaned_data['number']) and \
                Client.objects.filter(birth_date=form.cleaned_data['birth_date']):
            form.add_error(None, 'We have this client.')
            logger.error(f'Failed to create client by {self.request.user.username}!')
            return self.form_invalid(form)

        if not re.fullmatch(r"^[A-z '-]+$", form.cleaned_data['name']):
            form.add_error(None, 'Its not name.')
            logger.error(f'Failed to create client by {self.request.user.username}!')
            return self.form_invalid(form)

        date1 = form.cleaned_data['birth_date']
        dateTimeNow = datetime.date.today()
        dateInPast = datetime.date(1923, 12, 31)

        if ((dateTimeNow < date1) or (date1 < dateInPast)):
            form.add_error(None, 'Birth date in future or in the past.')
            logger.error(f'Failed to create birth_date by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Client was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Failed to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
class ClientUpdate(UpdateView):
    model = Client
    fields = ['name', 'number', 'birth_date']
    success_url = reverse_lazy('client')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Client.objects.filter(name=form.cleaned_data['name']) and \
                Client.objects.filter(number=form.cleaned_data['number']) and \
                Client.objects.filter(birth_date=form.cleaned_data['birth_date']):
            form.add_error(None, 'We have this client.')
            logger.error(f'Failed to create client by {self.request.user.username}!')
            return self.form_invalid(form)

        if not re.fullmatch(r"^[A-z '-]+$", form.cleaned_data['name']):
            form.add_error(None, 'Its not name.')
            logger.error(f'Failed to create client by {self.request.user.username}!')
            return self.form_invalid(form)

        date1 = form.cleaned_data['birth_date']
        dateTimeNow = datetime.date.today()
        dateInPast = datetime.date(1923, 12, 31)

        if ((dateTimeNow < date1) or (date1 < dateInPast)):
            form.add_error(None, 'Birth date in future or in the past.')
            logger.error(f'Failed to create birth_date by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Client was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Failed to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client')


# Shedule#########################
@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class SheduleCreate(CreateView):
    model = Shedule
    fields = ['doctor', 'client', 'service', 'room', 'date']
    success_url = reverse_lazy('shedule')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Shedule.objects.filter(doctor=form.cleaned_data['doctor']) and \
                Shedule.objects.filter(client=form.cleaned_data['client']) and \
                Shedule.objects.filter(service=form.cleaned_data['service']) and\
                Shedule.objects.filter(date=form.cleaned_data['date']):
            form.add_error(None, 'We have this shedule.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        if form.cleaned_data['doctor'] == None or form.cleaned_data['client'] == None or \
                form.cleaned_data['service'] == None:
            form.add_error(None, 'Shedule have empty field.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        date1 = form.cleaned_data['date']
        dateTimeNow = datetime.date.today()
        dateInFuture = datetime.date(2023, 8, 30)

        if ((dateTimeNow > date1) or (date1 > dateInFuture)):
            form.add_error(None, 'Date in past or the date is too far away.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Shedule was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Shedule to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
class SheduleUpdate(UpdateView):
    model = Shedule
    fields = ['doctor', 'client', 'service', 'room', 'date']
    success_url = reverse_lazy('shedule')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Shedule.objects.filter(doctor=form.cleaned_data['doctor']) and \
                Shedule.objects.filter(client=form.cleaned_data['client']) and \
                Shedule.objects.filter(service=form.cleaned_data['service']) and\
                Shedule.objects.filter(date=form.cleaned_data['date']):
            form.add_error(None, 'We have this shedule.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')

            return self.form_invalid(form)
        if form.cleaned_data['doctor'] == None or form.cleaned_data['client'] == None or \
                form.cleaned_data['service'] == None:
            form.add_error(None, 'Shedule have empty field.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        date1 = form.cleaned_data['date']
        dateTimeNow = datetime.date.today()
        dateInFuture = datetime.date(2023, 8, 30)

        if ((dateTimeNow > date1) or (date1 > dateInFuture)):
            form.add_error(None, 'Date in past or the date is too far away.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Shedule was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Shedule to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
class SheduleDelete(DeleteView):
    model = Shedule
    success_url = reverse_lazy('shedule')


class DoctortForm(forms.Form):
    num_validetor = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")
    name_validator = RegexValidator(regex=r"^[A-z '-]+$")
    # validate_name = RegexValidator(regex=r"/^[a-z ,.'-]+$/i")
    name = forms.CharField(max_length=20, validators=[name_validator])
    number = forms.CharField(max_length=30, validators=[num_validetor], help_text="+375 (29) xxx-xx-xx")
    password = forms.CharField(min_length=2, widget=forms.PasswordInput())


class ServiceDetailsView(View):
    @staticmethod
    def get(request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            raise Http404("Service doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/service_detail.html',
            context={'service': service, }
        )


@method_decorator(login_required, name='dispatch')
class ServiceCreate(CreateView):
    model = Service
    fields = ['procedure', 'price']
    success_url = reverse_lazy('service')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Service.objects.filter(procedure=form.cleaned_data['procedure']):
            form.add_error(None, 'We have this service.')
            logger.error(f'Failed to create service by {self.request.user.username}!')
            return self.form_invalid(form)

        if not re.fullmatch(r"^[A-z ,'-]+$", form.cleaned_data['procedure']):
            form.add_error(None, 'Its not procedure.')
            logger.error(f'Failed to create service by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Service was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Service to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service')


def UserRegistration(request):
    if request.method == "POST":
        doctorForm = DoctortForm(request.POST)
        if doctorForm.is_valid():
            user = User()
            user.username = doctorForm.cleaned_data['name']
            user.password = make_password(doctorForm.cleaned_data['password'])
            if User.objects.filter(username=user.username).exists():
                logger.error(f'Failed to add doctor ')
                doctorForm.add_error(None, "We have this user")
            else:
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
        context={'form': doctorForm, })


class ServiceListView(generic.ListView):
    model = Service
    context_object_name = 'service_list'
    template_name = 'CosmetologyApp/service.html'


@method_decorator(login_required, name='dispatch')
class ClientListView(generic.ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = 'CosmetologyApp/client.html'


@method_decorator(login_required, name='dispatch')
class DoctorListView(generic.ListView):
    model = Doctor
    context_object_name = 'doctor_list'
    template_name = 'CosmetologyApp/doctor.html'


@method_decorator(login_required, name='dispatch')
class SheduleListView(generic.ListView):
    model = Shedule
    context_object_name = 'shedule_list'
    template_name = 'CosmetologyApp/shedule.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class DiagramView(View):
    @staticmethod
    def get(request):
        services = Service.objects.all()
        fodder_types = list(Service.objects.values_list('procedure', flat=True))
        general_daily_feeds = []

        for service in services:
            shedules = Shedule.objects.filter(service=service)

            count = 0
            for shedule in shedules:
                count += 1

            general_daily_feeds.append(count)

        data = Bar(x=fodder_types, y=general_daily_feeds,
                   marker=dict(color=['pink', 'gray', 'white']))
        layout = Layout(title='Fodders and their general daily feed',
                        xaxis=dict(title='services'),
                        yaxis=dict(title='count of buy'))
        fig = Figure(data=data, layout=layout)
        plot_div = fig.to_html(full_html=False)

        return render(
            request,
            'CosmetologyApp/diagram.html',
            context={'plot_div': plot_div, }
        )


class StaticInfoView(View):
    @staticmethod
    def get(request):
        client_count = Client.objects.all().count()
        doctor_count = Doctor.objects.all().count()
        priems_count = Shedule.objects.all().count()
        service_count = Service.objects.all().count()
        last_used_service = Shedule.objects.latest('service')

        services = Service.objects.all()
        general_daily_feeds = []
        for service in services:
            shedules = Shedule.objects.filter(service=service)

            count = 0
            for shedule in shedules:
                count += 1

            general_daily_feeds.append((service.procedure, count))
        sorted_data = sorted(general_daily_feeds, key=lambda x: x[1], reverse=True)
        service = sorted_data[0][0]

        context = {
            'client_count': client_count,
            'doctor_count': doctor_count,
            'priems_count': priems_count,
            'service_count': service_count,
            'latest_proc': last_used_service,
            'pop_service': service
        }

        return render(
            request,
            'CosmetologyApp/static_info.html',
            context
        )


def formatted_datetime():
    current_datetime = datetime.now()
    result = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    return str(result)
