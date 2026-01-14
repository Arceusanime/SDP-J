from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Race, Ticket, Booking

admin.site.register(Race)
admin.site.register(Ticket)
admin.site.register(Booking)
