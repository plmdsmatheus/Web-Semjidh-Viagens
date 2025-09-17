from django.urls import path
from . import views

urlpatterns = [
    path('listar_viagens/', views.listar_viagens, name='listar_viagens'),
    path('solicitar_viagem/', views.solicitar_viagem, name='solicitar_viagem'),
    path('designar_motorista/<int:viagem_id>/', views.designar_motorista, name='designar_motorista'),
    path('cadastrar_motorista/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('listar_motoristas/', views.listar_motoristas, name='listar_motoristas'),
    path('<int:id>/apagar/', views.apagar_viagem, name='apagar_viagem'),
    path('motorista/<int:id>/apagar/', views.apagar_motorista, name='apagar_motorista'),
    path('exportar_viagens/', views.exportar_viagens, name='exportar_viagens'),
    path('listar_carros/', views.listar_carros, name='listar_carros'),
    path('carro/<int:id>/apagar/', views.apagar_carro, name='apagar_carro'),
    path('cadastrar_carro/', views.cadastrar_carro, name='cadastrar_carro'),
    path('designar_carro/<int:viagem_id>/', views.designar_carro, name='designar_carro'),
]
