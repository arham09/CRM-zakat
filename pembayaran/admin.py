from django.contrib import admin
from .models import Donasi, JenisDonasi

# Register your models here.
admin.site.register(Donasi)
admin.site.register(JenisDonasi)