from django.contrib import admin

# Register your models here.
from app_musicos.models import Instrumentos, Musicos, Notas

admin.site.register(Instrumentos)
admin.site.register(Musicos)
admin.site.register(Notas)
