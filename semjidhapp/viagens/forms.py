from django import forms
from .models import Viagem, Motorista

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['destino', 'data_ida', 'local_partida', 'horario_ida', 'data_volta', 'horario_volta', 'servidores', 'setor', 'solicitante', 'processo']
        widgets = {
            'destino': forms.TextInput(attrs={
                'placeholder': 'Digite para onde será a viagem',
                'type': 'text',
                'class': 'form-control'
            }),
            'data_ida': forms.DateInput(format='%d/%m/%Y', attrs={
                'placeholder': 'DD/MM/YYYY',
                'type': 'text',
                'class': 'form-control'
            }),
            'local_partida': forms.TextInput(attrs={
                'placeholder': 'Qual ponto inicial da viagem?',
                'type': 'text',
                'class': 'form-control'
            }),
            'horario_ida': forms.TimeInput(format='%H:%M', attrs={
                'placeholder': 'HH:MM',
                'type': 'time',
                'class': 'form-control'
            }),
            'data_volta': forms.DateInput(format='%d/%m/%Y', attrs={
                'placeholder': 'DD/MM/YYYY',
                'type': 'text',
                'class': 'form-control'
            }),
            'horario_volta': forms.TimeInput(format='%H:%M', attrs={
                'placeholder': 'HH:MM',
                'type': 'time',
                'class': 'form-control'
            }),
            'servidores': forms.TextInput(attrs={
                'placeholder': 'Digite os nomes dos servidores separados por vírgula',
                'class': 'form-control'
            }),
            'setor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'solicitante': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do solicitante',
                'class': 'form-control'
            }),
            'processo': forms.TextInput(attrs={
                'placeholder': 'Digite o número de processo, se houver',
                'class': 'form-control'
            })
        }
        processo = forms.CharField(required=False)

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do Motorista',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email do Motorista',
                'class': 'form-control'
            })
        }
