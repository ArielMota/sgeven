# Generated by Django 5.1.5 on 2025-01-20 06:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_inicio', models.DateTimeField(verbose_name='Data de Início')),
                ('data_fim', models.DateTimeField(verbose_name='Data de Término')),
                ('local', models.CharField(blank=True, max_length=255, null=True, verbose_name='Local')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Organizador')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('data_inscricao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscrição')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='evento.evento', verbose_name='Evento')),
            ],
        ),
    ]
