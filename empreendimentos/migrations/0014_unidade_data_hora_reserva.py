# Generated by Django 4.2.7 on 2023-12-04 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0013_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='data_hora_reserva',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
