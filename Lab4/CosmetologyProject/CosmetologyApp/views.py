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
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from plotly.graph_objects import Bar, Layout, Figure
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, \
    HttpResponseBadRequest
import datetime

from django.urls import reverse_lazy
from django.views import generic, View
import requests
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Service, Client, Doctor, Shedule, Doctor_Category, Vacancy, Promocode, Rewiew

logger = logging.getLogger(__name__)


def is_superuser(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseBadRequest()
        return view_func(request, *args, **kwargs)
    return wrapper
class HomeView(View):
    @staticmethod
    def get(request):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        image_url = response.json()['message']

        response = requests.get('https://www.boredapi.com/api/activity')
        act = response.json()['activity']
        last_add_service=Service.objects.latest('procedure')

        context = {
            'image_url': image_url,
            'activity': act,
            'latest_add_serv': last_add_service,
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
    def get(request, pk):
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            raise Http404("client doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/client_detail.html',
            context={'client': client, }
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(is_superuser, name='dispatch')
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
@method_decorator(is_superuser, name='dispatch')
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
@method_decorator(is_superuser, name='dispatch')
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
@method_decorator(is_superuser, name='dispatch')
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

        if form.cleaned_data['doctor'] is None or form.cleaned_data['client'] is None or \
                form.cleaned_data['service'] is None:
            form.add_error(None, 'Shedule have empty field.')
            logger.error(f'Failed to create shedule by {self.request.user.username}!')
            return self.form_invalid(form)

        date1 = form.cleaned_data['date']
        dateTimeNow = datetime.date.today()
        dateInFuture = datetime.date(2023, 12, 30)

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
@method_decorator(is_superuser, name='dispatch')
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
        dateInFuture = datetime.date(2023, 12, 30)

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
@method_decorator(is_superuser, name='dispatch')
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
    photo_link = forms.CharField(min_length=2)


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
@method_decorator(is_superuser, name='dispatch')
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
@method_decorator(is_superuser, name='dispatch')
class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service')

class RewiewForm(forms.Form):
    name_validator = RegexValidator(regex=r"^[A-z '-]+$")
    reviewer = forms.CharField(max_length=20, validators=[name_validator])
    rate = forms.CharField(max_length=2, help_text="rate from 1 to 10")
    text = forms.CharField(help_text="your review")

def RewiewCreate(request):
    if request.method == "GET":
        form = RewiewForm()
        return render(request, "CosmetologyApp/rewiew_form.html", {'form':form})
    if request.method == "POST":
        form = RewiewForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                reviewer = form.cleaned_data['reviewer']
                rate = form.cleaned_data['rate']
                text = form.cleaned_data['text']
                creation_date = datetime.date.today()

                Rewiew.objects.create(
                    reviewer=reviewer,
                    rate=rate,
                    text=text,
                    creation_date=creation_date
                )

                return HttpResponseRedirect('/CosmetologyApp/rewiew/')
        else:
            return render(request, "CosmetologyApp/rewiew_form.html", {'form': form})

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
                doctor.photo = doctorForm.cleaned_data['photo_link']
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
@method_decorator(is_superuser, name='dispatch')
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

class AboutCompanyInfoView(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/about_company.html',
            context
        )
class News(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/news.html',
            context
        )
class ancient_cosmetic(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/ancient_cosmetic.html',
            context
        )
class injectable_procedures(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/injectable_procedures.html',
            context
        )

class Influence_of_technology(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/Influence_of_technology.html',
            context
        )
class Mens_grooming(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/Mens_grooming.html',
            context
        )
class faq(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/faq.html',
            context
        )

class rewiew(generic.ListView):
    model = Rewiew
    context_object_name = 'rewiew_list'
    template_name = 'CosmetologyApp/rewiew.html'




class private_policy(View):
    @staticmethod
    def get(request):
        context = {}
        return render(
            request,
            'CosmetologyApp/private_policy.html',
            context
        )
class vacancy_View(generic.ListView):
    model = Vacancy
    context_object_name = 'vacancy_list'
    template_name = 'CosmetologyApp/vacancy.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(is_superuser, name='dispatch')
class VacancyCreate(CreateView):
    model = Vacancy
    fields = ['job_character', 'experience', 'description', 'salary']
    success_url = reverse_lazy('vacancy')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Vacancy.objects.filter(job_character=form.cleaned_data['job_character']):
            form.add_error(None, 'We have this job_character.')
            logger.error(f'Failed to create vacancy by {self.request.user.username}!')
            return self.form_invalid(form)

        if not re.fullmatch(r"^[A-z ,'-]+$", form.cleaned_data['job_character']):
            form.add_error(None, 'Its not job_character.')
            logger.error(f'Failed to create vacancy by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Vacancy was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Vacancy to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
@method_decorator(is_superuser, name='dispatch')
class VacancyDelete(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancy')

class VacancyDetailsView(View):
    @staticmethod
    def get(request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise Http404("Vacancy doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/vacancy_detail.html',
            context={'vacancy': vacancy, }
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

class PromocodeView(generic.ListView):
    model = Promocode
    context_object_name = 'promocode_list'
    template_name = 'CosmetologyApp/promocode.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.date.today()

        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(is_superuser, name='dispatch')
class PromocodeCreate(CreateView):
    model = Promocode
    fields = ['code', 'start_date', 'expiration_date', 'sale']
    success_url = reverse_lazy('promocode')

    def form_valid(self, form):
        # form.instance.staffer = Staffer.objects.filter(username=self.request.user.username).first()
        if Promocode.objects.filter(code=form.cleaned_data['code']) and \
                Shedule.objects.filter(start_date=form.cleaned_data['start_date']) and \
                Shedule.objects.filter(expiration_date=form.cleaned_data['expiration_date']):
            form.add_error(None, 'We have this promocode.')
            logger.error(f'Failed to create promocode by {self.request.user.username}!')
            return self.form_invalid(form)

        if form.cleaned_data['code'] is None or form.cleaned_data['expiration_date'] is None or \
                form.cleaned_data['start_date'] is None:
            form.add_error(None, 'Promocode have empty field.')
            logger.error(f'Failed to create promocode by {self.request.user.username}!')
            return self.form_invalid(form)

        date_start = form.cleaned_data['start_date']
        date_end = form.cleaned_data['expiration_date']
        dateInPast = datetime.date(2000, 8, 30)
        dateInFuture = datetime.date(2024, 8, 30)

        if (date_start > dateInFuture or (date_end<date_start) or(date_start<dateInPast)):
            form.add_error(None, 'Check dates')
            logger.error(f'Failed to create promocode by {self.request.user.username}!')
            return self.form_invalid(form)

        try:
            response = super().form_valid(form)

            logger.info(f'Promocode was created successfully by {self.request.user.username}.')
            return response
        except Exception:
            logger.error(f'Promocode to create client by {self.request.user.username}!')
            raise


@method_decorator(login_required, name='dispatch')
@method_decorator(is_superuser, name='dispatch')
class PromocodeDelete(DeleteView):
    model = Promocode
    success_url = reverse_lazy('promocode')

class PromocodeDetailsView(View):
    @staticmethod
    def get(request, id):
        try:
            promocode = Promocode.objects.get(id=id)
        except Promocode.DoesNotExist:
            raise Http404("Promocode doesn't exist :(")
        return render(
            request,
            'CosmetologyApp/promocode_detail.html',
            context={'promocode': promocode, }
        )
