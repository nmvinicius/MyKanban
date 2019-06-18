from django.db import models
from django.utils import timezone


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    estado = models.CharField(max_length=10, default="Afazer")
    dtstatus = models.DateTimeField(default=timezone.now)
    dtprazo = models.DateTimeField()

    def __str__(self):
        return self.titulo + " - " + self.estado
