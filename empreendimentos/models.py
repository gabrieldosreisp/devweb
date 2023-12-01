from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth import get_user_model


class Empreendimento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    
    TIPOS_EMPREENDIMENTO = (
        ('predio', 'Prédio'),
        ('loteamento', 'Loteamento'),
    )
    
    tipo_empreendimento = models.CharField(
        max_length=20,
        choices=TIPOS_EMPREENDIMENTO,
        default='predio',
    )

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    reservado_por = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, related_name='unidades')
    numero = models.CharField(max_length=10)
    descricao = models.TextField(100)
    preco = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=[
        ('disponivel', 'Disponível'),
        ('reservada', 'Reservar'),
        ('vendida', 'Vender'),
    ])
    def nome_reservado_por(self):
        return self.reservado_por.username if self.reservado_por else "N/A"
    def __str__(self):
        return f'Unidade {self.numero} - {self.empreendimento.nome}'