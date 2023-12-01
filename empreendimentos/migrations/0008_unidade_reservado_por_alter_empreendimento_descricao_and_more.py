# Generated by Django 4.2.7 on 2023-11-30 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empreendimentos', '0007_alter_empreendimento_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='reservado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='descricao',
            field=models.TextField(verbose_name=100),
        ),
    ]
