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

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('importar_excel/', self.importar_excel, name='importar_excel'),
        ]
        return my_urls + urls

    def importar_excel(self, request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['excel_file']:
            empreendimento = self.get_object(request, kwargs['object_id'])
            excel_file = request.FILES['excel_file']

            # Lógica para importar unidades do Excel
            unidades_df = pd.read_excel(excel_file)
            for _, row in unidades_df.iterrows():
                Unidade.objects.create(
                    empreendimento=empreendimento,
                    numero=row['numero'],
                    descricao=row['descricao'],
                    preco=row['preco'],
                    status=row['status']
                )

            self.message_user(request, f'Unidades importadas com sucesso do arquivo: {excel_file.name}')
            return render(request, 'admin/empreendimentos/importar_excel_response.html', {'empreendimento': empreendimento})

        return render(request, 'admin/empreendimentos/importar_excel_form.html', {'empreendimento': self.get_object(request, kwargs['object_id'])})

admin.site.register(Empreendimento, EmpreendimentoAdmin)
