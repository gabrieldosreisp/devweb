# Generated by Django 4.2.7 on 2023-11-29 23:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0006_auto_20231129_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='descricao',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='descricao',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
