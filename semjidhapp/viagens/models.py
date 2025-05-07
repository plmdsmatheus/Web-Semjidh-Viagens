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
    horario_ida = models.TimeField(verbose_name='Horário de ida')
    data_volta = models.DateField()
    horario_volta = models.TimeField(verbose_name='Previsão de retorno')
    servidores = models.TextField()
    motorista = models.ForeignKey(Motorista, null=True, blank=True, on_delete=models.SET_NULL)
    solicitante = models.CharField(null=False, blank=False, max_length=30)
    processo = models.CharField(blank=True, null=True, max_length=23)
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Atribuída', 'Atribuída'), ('Concluída', 'Concluída')], default='Pendente')
    criada_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.destino} - {self.data_ida}"
