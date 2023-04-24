from django.contrib import admin
from .models import Marital, Profile

# Register your models here.
admin.site.register([Marital, Profile])