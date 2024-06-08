from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from.models import Aluno
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, FiltroDataForm
from .models import Aluno, RegistroPresenca
from datetime import date
from django.utils import timezone


def index(request):
    alunos = Aluno.objects.all()
    data_atual = timezone.now().date()
    registros_presenca = RegistroPresenca.objects.filter(data=data_atual)
    
    # Cria um dicionário com o status de presença de cada aluno
    presenca_alunos = {}
    for aluno in alunos:
        try:
            # Tenta buscar o registro de presença do aluno para o dia atual
            registro_presenca = registros_presenca.get(aluno=aluno)
            presenca_alunos[aluno] = registro_presenca.presente
        except RegistroPresenca.DoesNotExist:
            # Se não houver registro de presença para o aluno, assume-se que está ausente
            presenca_alunos[aluno] = False
    
    context = {
        'presenca_alunos': presenca_alunos
    }
    return render(request, 'index.html', context)


def update_presence(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    data_atual = timezone.now().date()
    
    # Busca ou cria o registro de presença para o aluno na data atual
    registro_presenca, _ = RegistroPresenca.objects.get_or_create(aluno=aluno, data=data_atual)
    
    # Inverte o status de presença e salva no banco de dados
    registro_presenca.presente = not registro_presenca.presente
    registro_presenca.save()
    
    return redirect('index')


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'adicionar_aluno.html', {'form': form})

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'editar_aluno.html', {'form': form})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'confirmar_exclusao.html', {'aluno': aluno})


def visualizar_presenca(request):
    registros_presenca = None

    if request.method == 'POST':
        form = FiltroDataForm(request.POST)
        if form.is_valid():
            data_filtro = form.cleaned_data['data_filtro']
            registros_presenca = RegistroPresenca.objects.filter(data=data_filtro)
    else:
        data_filtro = request.GET.get('data_filtro')
        form = FiltroDataForm(initial={'data_filtro': data_filtro})
        if data_filtro:
            registros_presenca = RegistroPresenca.objects.filter(data=data_filtro)
        else:
            registros_presenca = RegistroPresenca.objects.all()

    context = {
        'form': form,
        'registros_presenca': registros_presenca
    }
    return render(request, 'visualizar_presenca.html', context)