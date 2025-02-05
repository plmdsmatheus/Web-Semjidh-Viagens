from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Viagem, Motorista
from .forms import ViagemForm, MotoristaForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import csv

@login_required
def listar_viagens(request):
    viagens = Viagem.objects.all().order_by('-criada_em')
    for viagem in viagens:
        viagem.servidores_lista = viagem.servidores.split(',')
    return render(request, 'viagens/listar_viagens.html', {'viagens': viagens})

def solicitar_viagem(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Viagem solicitada com sucesso!') 
            return render(request, 'viagens/solicitar_viagem.html', {'form': form}) 
    else:
        form = ViagemForm()
    
    return render(request, 'viagens/solicitar_viagem.html', {'form': form})

@login_required
def designar_motorista(request, viagem_id):
    viagem = Viagem.objects.get(id=viagem_id)
    motoristas = Motorista.objects.all()
    if request.method == 'POST':
        motorista_id = request.POST.get('motorista')
        motorista = Motorista.objects.get(id=motorista_id)
        viagem.motorista = motorista
        viagem.status = 'Atribuída'
        viagem.save()

        assunto = "VIAGEM SOLICITADA!"
        corpo_email = f""" 
                Você foi designado para a seguinte viagem:

                Destino: {viagem.destino}
                Data de ida: {viagem.data_ida.strftime('%d/%m/%Y')}
                Data de volta: {viagem.data_volta.strftime('%d/%m/%Y')}
                Solicitante: {viagem.solicitante}

                Favor confirmar sua disponibilidade.
                """
        
        send_mail(
            assunto,
            corpo_email,
            settings.DEFAULT_FROM_EMAIL,
            [motorista.email],
            fail_silently=False,
        )
        messages.success(request, 'Motorista designado com sucesso e notificado por e-mail!')
        return redirect('listar_viagens')
    return render(request, 'viagens/designar_motorista.html', {'viagem': viagem, 'motoristas': motoristas})

@login_required
def cadastrar_motorista(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o motorista no banco de dados
            
            messages.success(request, 'Motorista cadastrado com sucesso!')
            return redirect('listar_motoristas')  # Redireciona para a página de listagem dos motoristas
    else:
        form = MotoristaForm()
    
    return render(request, 'viagens/cadastrar_motorista.html', {'form': form})

@login_required
def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    return render(request, 'viagens/listar_motoristas.html', {'motoristas': motoristas})

def home(request):
    return render(request, 'home.html')

@login_required
def apagar_viagem(request, id):
    viagem = get_object_or_404(Viagem, id=id)

    if request.method == 'POST':
        assunto = "VIAGEM CANCELADA!"
        corpo_email = f""" Uma viagem foi cancelada.
                    Viagem do dia {viagem.data_ida.strftime('%d/%m/%Y')} de destino {viagem.destino} foi cancelada
                    """
        send_mail(
            assunto,
            corpo_email,
            settings.DEFAULT_FROM_EMAIL,
            [viagem.motorista.email],
            fail_silently=False,
        )
        viagem.delete()
        return redirect('listar_viagens')  # Redireciona para a lista de viagens

    # Caso seja um GET, você pode exibir uma confirmação ou mensagem
    return render(request, 'confirmar_apagar.html', {'viagem': viagem})

@login_required
def apagar_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)

    if request.method == 'POST':
        motorista.delete()
        return redirect('listar_motoristas')
    

@login_required
def exportar_viagens(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="viagens_semjidh.csv"'

    writer = csv.writer(response)
    
    writer.writerow(['ID', 'Destino', 'Data de Ida', 'Data de Volta', 'Solicitante', 'Motorista'])

    viagens = Viagem.objects.all()

    for viagem in viagens:
        writer.writerow([
            viagem.id,
            viagem.destino,
            viagem.data_ida.strftime('%d/%m/%Y'),  # Formatação da data
            viagem.data_volta.strftime('%d/%m/%Y'),
            viagem.solicitante,
            viagem.motorista.nome if viagem.motorista else 'Sem motorista' 
        ])

    return response