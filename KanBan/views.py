from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tarefa
from .forms import FormTarefa


def index(request):
    Afazer = Tarefa.objects.filter(estado="Afazer")
    Fazendo = Tarefa.objects.filter(estado="Fazendo")
    Concluido = Tarefa.objects.filter(estado="Concluido")
    return render(request, 'index.html', {'Afazer': Afazer, "Fazendo": Fazendo, "Concluido": Concluido})


def newTarefa(request):
    if request.method == "POST":
        form = FormTarefa(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect('/')
    else:
        form = FormTarefa()
    return render(request, 'newTarefa.html', {'form': form})


def upEstado(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    print(tarefa)
    if tarefa.estado == "Afazer":
        print(tarefa.estado)
        tarefa.estado = "Fazendo"
        print(tarefa.estado)
    elif tarefa.estado == "Fazendo":
        tarefa.estado = "Concluido"
    tarefa.save()
    print(tarefa)
    return redirect('/')


def delTarefa(request, pk):
    Tarefa.objects.get(pk=pk).delete()
    return redirect('/')
