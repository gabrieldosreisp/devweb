# Generated by Django 4.2.7 on 2023-12-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0015_remove_unidade_data_hora_reserva_delete_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade',
            name='descricao',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='status',
            field=models.CharField(choices=[('disponivel', 'Disponível'), ('reservada', 'Reservado'), ('vendida', 'Vendido')], max_length=20),
        ),
    ]