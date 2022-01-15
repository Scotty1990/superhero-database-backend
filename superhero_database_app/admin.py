from django.contrib import admin
from .models import SuperHero, SuperVillain

# Register your models here.
admin.site.register(SuperHero)
admin.site.register(SuperVillain)