# Generated by Django 4.2.7 on 2023-12-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0009_empreendimento_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/empreendimento_imagens/'),
        ),
    ]