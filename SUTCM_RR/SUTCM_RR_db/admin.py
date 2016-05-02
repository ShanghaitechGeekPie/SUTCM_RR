from django.contrib import admin

from .models import Resource, Reservation

admin.site.register(Resource)
admin.site.register(Reservation)