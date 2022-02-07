from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento_Agendado(models.Model):
    titulo_do_evento_agendado = models.CharField(max_length=100,
                                                 verbose_name="Titulo")
    decricao_do_evento_agendado = models.TextField(blank=True,
                                                   null=True,
                                                   verbose_name="Descrição")
    data_do_evento_agendado = models.DateTimeField(verbose_name="Data do Evento")
    data_da_criacao_do_evento_agendado = models.DateTimeField(auto_now=True,
                                                              verbose_name="Data de Criação")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Eventos Agendados"

    def __str__(self):
        return self.titulo_do_evento_agendado
