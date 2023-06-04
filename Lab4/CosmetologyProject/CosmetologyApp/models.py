from django.db import models
import datetime
import re
import uuid
from wsgiref.validate import validator
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


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
        ordering = ['number']
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.number
class Doctor(models.Model):
    num_validetor = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20, validators=[num_validetor], default='+375 (29) xxx-xx-xx')
    # category = models.ForeignKey(Doctor_Category, on_delete=models.SET_NULL, null=True, blank=True,
    #                              related_name='doctor_category')


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self) -> str:
        return f'{self.name}'
class Service(models.Model):
    procedure = models.CharField(max_length=30)
    price = models.FloatField(validators=[MinValueValidator(1.00), MaxValueValidator(150.00)])

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.procedure}'
class Client(models.Model):
    num_validetor = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20,  help_text='+375 (29) xxx-xx-xx')
    birth_date = models.DateField(null=True, blank=False)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return f'{self.name}, {self.number}'

class Shedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='doctor_in_shedule')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='client_in_shedule')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='shedule_service', null=True, blank=True,
                                )
    room = models.IntegerField(validators=[MaxValueValidator(20), MinValueValidator(1)])
    date = models.DateField(null=True,blank=False)


    class Meta:
        verbose_name = "Shedule"
        verbose_name_plural = "Shedules"

    def __str__(self) -> str:
        return f'{self.doctor} {self.client}{self.service} {self.room}{self.date}'

class Sale(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='sale_servise')
    count = models.IntegerField()

    class Meta:
        ordering = ['service', 'count']
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return "\nService: "+str(self.service) + "\nCount_sale: "+str(self.count)


