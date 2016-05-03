from django.contrib import admin

from .models import Category, Department, Room, Reservation

admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Reservation)