from django.db import models
from django.contrib.auth.models import User

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Viagem(models.Model):
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    servidores = models.TextField()
    motorista = models.ForeignKey(Motorista, null=True, blank=True, on_delete=models.SET_NULL)
    solicitante = models.CharField(null=False, blank=False, max_length=30)
    processo = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Atribuída', 'Atribuída'), ('Concluída', 'Concluída')], default='Pendente')
    criada_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.destino} - {self.data_ida}"
