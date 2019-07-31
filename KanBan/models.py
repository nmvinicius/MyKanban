from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    estado = models.CharField(max_length=10, default="Afazer")
    dtcriacao = models.DateTimeField(default=timezone.now)
    dtprazo = models.DateTimeField(default=timezone.now)
    dtconcluzao = models.DateTimeField(null=True)


    def __str__(self):
        return self.titulo + " - " + self.estado
