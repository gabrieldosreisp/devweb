# Generated by Django 4.2.7 on 2023-12-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0008_unidade_reservado_por_alter_empreendimento_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empreendimento',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='empreendimento_imagens/'),
        ),
    ]
