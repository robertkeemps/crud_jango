from django.shortcuts import render, redirect
from .models import Estudante
from .forms import EstudanteForm

# Create your views here.
def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    dicionario = {'registros': estudantes}
    return render(request, 'listagem.html', context=dicionario)

def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'adicionar.html', {'form': form})

def editarEstudante(request, id):
    estudante = Estudante.objects.get(id=id)
    form = EstudanteForm(request.POST or None, request.FILES or None, instance=estudante)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'editar.html', {'form': form})

def deletarEstudante(request, id):
    estudante = Estudante.objects.get(id=id)
    if request.method == 'POST':
        estudante.delete()
        return redirect('/')
    return render(request, 'deletar.html', {'estudante': estudante})

def visualizarEstudante(request, id):
    estudante = Estudante.objects.get(id=id)
    return render(request, 'visualizar.html', {'estudante': estudante})