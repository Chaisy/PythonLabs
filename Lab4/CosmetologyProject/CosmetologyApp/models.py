from django.db import models

import re
import uuid
from wsgiref.validate import validator
from django.db import models
from django.core.validators import RegexValidator


class Doctor_Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Doc_Category"
        verbose_name_plural = "Doc_Categories"

    def __str__(self):
        return self.category

class Room(models.Model):
    number = models.IntegerField()

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.number

class Doctor(models.Model):
    num_validetor = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20, validators=[num_validetor], default='+375 (29) xxx-xx-xx')
    category = models.ForeignKey(Doctor_Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='doctor_category')


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self) -> str:
        return self.name + "\n" + self.number

class Service(models.Model):
    procedure = models.CharField(max_length=30)
    price = models.FloatField()

    class Meta:
        ordering = ['procedure', 'price']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.procedure} {self.price}'

class Client(models.Model):
    num_validetor = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")
    adress_validator = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")#!!!!!!!!!!!!!

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20, validators=[num_validetor], default='+375 (29) xxx-xx-xx')
    birth_date = models.DateField(null=True, blank=True)
    adress = models.CharField(max_length=100, validators=[adress_validator], default='Gikalo, 9')
    service = models.ManyToManyField(Service,   blank=True, related_name='servise_for_client')
    doctor = models.ManyToManyField(Doctor,  blank=True, related_name='doctor_for_client')

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return self.name + "\n" + self.number

class Shedule(models.Model):

    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='service_in_shedule')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='doctor_in_shedule')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='client_in_shedule')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='room_in_shedule')
    date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Shedule"
        verbose_name_plural = "Shedules"

    def __str__(self) -> str:
        return "\nDoctor: " + str(self.doctor) + "\nClient: " + str(self.client) \
            + "\n Service: " + str(self.service) + "\nRoom: " + str(self.room) + "\nDate: " + str(self.date)




class Sale(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='sale_servise')
    count = models.IntegerField()

    class Meta:
        ordering = ['service', 'count']
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return f'{self.service} {self.count}'


