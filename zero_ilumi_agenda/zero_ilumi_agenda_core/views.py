from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from zero_ilumi_agenda_core.models import Evento_Agendado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('nome_de_usuario')
        password = request.POST.get('senha_do_usuario')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou Senha Inválidos")
    return redirect('/')


@login_required(login_url='/login/')
def listar_eventos_agendados(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    eventos_do_usuario = Evento_Agendado.objects.filter(usuario=usuario)
    dados = {'eventos': eventos_do_usuario}
    return render(request, 'zero_ilumi_agenda.html', dados)


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento_Agendado.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        usuario = request.user
        titulo = request.POST.get('titulo_agendamento_novo')
        descricao = request.POST.get('input_descricao_agendamento_novo')
        data_do_evento = request.POST.get('data_do_evento_agendamento_novo')
        local_do_evento = request.POST.get('local_do_evento_agendamento_novo')
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento_Agendado.objects.get(id=id_evento)
            if usuario == evento.usuario:
                evento.titulo_do_evento_agendado = titulo
                evento.data_do_evento_agendado = data_do_evento
                evento.decricao_do_evento_agendado = descricao
                evento.save()
            # Evento_Agendado.objects.filter(id=id_evento).update(titulo_do_evento_agendado=titulo,
            #                                                     data_do_evento_agendado=data_do_evento,
            #                                                     decricao_do_evento_agendado=descricao)
        else:
            Evento_Agendado.objects.create(usuario=usuario,
                                           titulo_do_evento_agendado=titulo,
                                           decricao_do_evento_agendado=descricao,
                                           data_do_evento_agendado=data_do_evento,
                                           local_do_evento_agenda=local_do_evento)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento_Agendado.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento_Agendado.objects.filter(usuario=usuario).values('id', 'titulo_do_evento_agendado')
    return JsonResponse(list(evento), safe=False)



