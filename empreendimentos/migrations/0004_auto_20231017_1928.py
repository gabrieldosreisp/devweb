# Generated by Django 3.1.4 on 2023-10-17 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0003_auto_20231005_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='data_expiracao',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='data_reserva',
        ),
    ]
