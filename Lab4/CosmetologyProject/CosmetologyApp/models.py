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
    photo = models.CharField(max_length=1000, default="")


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self) -> str:
        return f'{self.name}'


class Service(models.Model):
    procedure = models.CharField(max_length=30)
    price = models.FloatField(validators=[MinValueValidator(1.00), MaxValueValidator(150.00)], default='0.00')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.procedure}'

class Vacancy(models.Model):
    job_character = models.CharField(max_length=50, help_text="enter job character")
    experience = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(60)], default='0', help_text="enter experience(years)")
    description = models.TextField(help_text="enter vacancy description")
    salary = models.FloatField(validators=[MinValueValidator(100.00), MaxValueValidator(1500.00)], default='0.00')

    def __str__(self):
        return f'{self.job_character}'

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
        return f'{self.service}'


class Sale(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='sale_servise')
    count = models.IntegerField()

    class Meta:
        ordering = ['service', 'count']
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return "\nService: "+str(self.service) + "\nCount_sale: "+str(self.count)


class Promocode(models.Model):
    code = models.CharField(max_length=50, help_text="enter Promocode")

    start_date = models.DateField()

    expiration_date = models.DateField()
    sale = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(100)], default='0')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class Rewiew(models.Model):
    reviewer = models.CharField(max_length=50, help_text="enter reviewer")

    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                       help_text="enter rate")

    text = models.TextField(help_text="enter review text")

    creation_date = models.DateField()

    def __str__(self):
        return self.reviewer

