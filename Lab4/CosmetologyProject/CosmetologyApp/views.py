from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime

from django.views import generic, View

from .models import Service, Client, Doctor, Shedule


def index(request):
    now = datetime.now()

    return render(
        request,
        "CosmetologyApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "CosmetologyApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )

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