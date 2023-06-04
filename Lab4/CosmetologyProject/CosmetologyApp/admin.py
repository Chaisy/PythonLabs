from django.contrib import admin
from .models import Doctor, Client, Doctor_Category, Service, Room, Sale, Shedule
# Register your models here.

# admin.site.register(Doctor)
admin.site.register(Doctor_Category)
admin.site.register(Room)
# admin.site.register(Client)
admin.site.register(Service) # услуга
admin.site.register(Shedule)
admin.site.register(Sale)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number')
    list_filter = ('name', 'number')
    search_fields = ['^name', '^number']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'birth_date')
    list_filter = ('name', 'number')
    search_fields = ['^name', '^number']








