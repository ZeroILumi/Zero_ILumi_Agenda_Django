from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.

class Evento_Agendado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_do_evento_agendado = models.CharField(max_length=100,
                                                 verbose_name="Titulo")
    decricao_do_evento_agendado = models.TextField(blank=True,
                                                   null=True,
                                                   verbose_name="Descrição")
    data_do_evento_agendado = models.DateTimeField(verbose_name="Data do Evento")
    data_da_criacao_do_evento_agendado = models.DateTimeField(auto_now=True,
                                                              verbose_name="Data de Criação")
    local_do_evento_agenda = models.CharField(max_length=100,
                                              verbose_name="Local do Evento",
                                              blank=True,
                                              null=True)

    class Meta:
        db_table = "Eventos Agendados"

    def __str__(self):
        return self.titulo_do_evento_agendado

    def get_data_do_evento_agendado(self):
        return self.data_do_evento_agendado.strftime('%d/%m/%Y as %H:%M')

    def get_data_do_evento_agendado_input(self):
        return self.data_do_evento_agendado.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_do_evento_agendado < datetime.now():
            return True
        else:
            return False

