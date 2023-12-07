from django.contrib import admin
from django.http import HttpResponse
import pandas as pd
from django.urls import path
from django.shortcuts import render
from .models import Empreendimento, Unidade

class UnidadeInline(admin.StackedInline ):
    model = Unidade
    extra = 1 # Define quantos formulários de unidades serão exibidos por padrão

class EmpreendimentoAdmin(admin.ModelAdmin):
    inlines = [UnidadeInline]
    
    list_display = ('nome', 'tipo_empreendimento', 'imagem', 'material_divulgacao')

    actions = ['alterar_status_disponivel', 'alterar_status_reservado', 'alterar_status_vendido']

    def alterar_status_disponivel(self, request, queryset):
        queryset.update(status='disponivel')
    alterar_status_disponivel.short_description = 'Liberar Unidade'

    def alterar_status_reservado(self, request, queryset):
        queryset.update(status='reservada')
    alterar_status_reservado.short_description = 'Reservar Unidade'

    def alterar_status_vendido(self, request, queryset):
        queryset.update(status='vendida')
    alterar_status_vendido.short_description = 'Vender Unidade'



admin.site.register(Empreendimento, EmpreendimentoAdmin)
