from django.db import models
from django.contrib.auth.models import User

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Viagem(models.Model):

    SETOR_CHOICES = [
        ('Gabinete',   'Gabinete'),
        ('Comunicação','Comunicação'),
        ('Adjunto',    'Adjunto'),
        ('Ouvidoria',  'Ouvidoria'),
        ('Procon',     'Procon'),
        ('CODIS',      'CODIS'),
        ('COEPPIR',    'COEPPIR'),
        ('SEJUV',      'SEJUV'),
        ('SPM',        'SPM'),
        ('CPDH',       'CPDH'),
        ('CORDE',      'CORDE'),
        ('ASJUR',      'ASJUR'),
        ('UIAG',       'UIAG'),
        ('UIFP',       'UIFP'),
    ]

    setor = models.CharField(
        max_length=12,
        choices=SETOR_CHOICES,
        verbose_name='Setor'
    )
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    local_partida = models.TextField(default='SEMJIDH')
    horario_ida = models.TimeField(null=True, blank=True, verbose_name='Horário de ida')
    data_volta = models.DateField()
    horario_volta = models.TimeField(null=True, blank=True, verbose_name='Previsão de retorno')
    servidores = models.TextField()
    motorista = models.ForeignKey(Motorista, null=True, blank=True, on_delete=models.SET_NULL)
    solicitante = models.CharField(null=False, blank=False, max_length=30)
    processo = models.CharField(blank=True, null=True, max_length=23)
    status = models.CharField(
        max_length=20,
        choices=[('Pendente', 'Pendente'), ('Atribuída', 'Atribuída'), ('Concluída', 'Concluída')],
        default='Pendente'
    )
    criada_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.destino} - {self.data_ida}"
