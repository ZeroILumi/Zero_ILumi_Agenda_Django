from django.contrib import admin
from .models import Evento_Agendado

# Register your models here.

class Evento_Agendado_Admin(admin.ModelAdmin):
    list_display = ('titulo_do_evento_agendado',
                    'data_do_evento_agendado',
                    'data_da_criacao_do_evento_agendado')
    list_filter = ('titulo_do_evento_agendado', 'usuario',)

admin.site.register(Evento_Agendado, Evento_Agendado_Admin)

