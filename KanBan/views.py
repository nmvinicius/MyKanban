from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tarefa
from django.utils import timezone
from .forms import FormTarefa


def index(request):
    if request.user.is_authenticated:
        Afazer = Tarefa.objects.filter(estado="Afazer", user=request.user).order_by('-dtcriacao')[:3]
        Planejando = Tarefa.objects.filter(estado="Planejando", user=request.user).order_by('-dtcriacao')[:3]
        Fazendo = Tarefa.objects.filter(estado="Fazendo", user=request.user).order_by('-dtcriacao')[:3]
        Concluido = Tarefa.objects.filter(estado="Concluido", user=request.user).order_by('-dtconcluzao')[:3]
        return render(request, 'index.html', {
            "Afazer": Afazer,
            "Planejando": Planejando,
            "Fazendo": Fazendo,
            "Concluido": Concluido
        })
    else:
        return redirect("account/login")


def newTarefa(request):
    if request.method == "POST":
        try:
            form = FormTarefa(request.POST)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
        except:
            return redirect('/new')
    else:
        form = FormTarefa()
        return render(request, 'newTarefa.html', {'form': form})


def upEstado(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    if tarefa.estado == "Afazer":
        tarefa.estado = "Planejando"
    elif tarefa.estado == "Planejando":
        tarefa.estado = "Fazendo"
    elif tarefa.estado == "Fazendo":
        tarefa.estado = "Concluido"
        tarefa.dtconcluzao = timezone.now()
    tarefa.save()
    return redirect('/')


def delTarefa(request, pk):
    Tarefa.objects.get(pk=pk).delete()
    return redirect('/')
