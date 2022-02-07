from django.shortcuts import render

# Create your views here.

def listar_eventos_agendados(request):
    render(request, 'zero_ilumi_agenda.html')
