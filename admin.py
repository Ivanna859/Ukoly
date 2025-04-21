from django.contrib import admin
from .models import Service, TeamMember, Reservation

admin.site.register(Service)
admin.site.register(TeamMember)
admin.site.register(Reservation)

