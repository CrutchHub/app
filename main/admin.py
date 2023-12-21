from django.contrib import admin
from .models import Adress, House, Apartment, Application

# Регистрация моделей в админке
admin.site.register(Adress)
admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(Application)