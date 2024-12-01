from django.contrib import admin
from .models import Profile,Status,Ticket

# Register your models here.

admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Ticket)