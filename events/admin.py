from django.contrib import admin
from events.models import Event, Reservation


admin.site.register(Event)
admin.site.register(Reservation)
