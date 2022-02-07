from django.contrib import admin
from zero_ilumi_agenda_core import models


# Register your models here.

class Evento_Agendado_Admin(admin.ModelAdmin):
    list_display = ('id', 'titulo_do_evento_agendado',
                    'data_do_evento_agendado',
                    'data_da_criacao_do_evento_agendado')
    list_filter = ('titulo_do_evento_agendado', 'usuario',)


admin.site.register(models.Evento_Agendado, Evento_Agendado_Admin)
