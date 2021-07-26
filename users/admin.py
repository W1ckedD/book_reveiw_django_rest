from django.contrib import admin
from .models import User, CurrentlyReading

admin.site.register(User)
admin.site.register(CurrentlyReading)