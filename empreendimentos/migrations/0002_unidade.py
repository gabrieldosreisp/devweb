# Generated by Django 3.1.4 on 2023-09-27 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('disponivel', 'Disponível'), ('reservada', 'Reservada'), ('vendida', 'Vendida')], max_length=20)),
                ('empreendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empreendimentos.empreendimento')),
            ],
        ),
    ]