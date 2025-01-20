from django.db import models
from django.contrib.auth.models import User

# Modelo de Evento
class Evento(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    organizador = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Organizador')
    data_inicio = models.DateTimeField(verbose_name='Data de Início')
    data_fim = models.DateTimeField(verbose_name='Data de Término')
    local = models.CharField(max_length=255, verbose_name='Local', blank=True, null=True)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    # Outros campos relevantes

    def __str__(self):
        return self.nome

# Modelo de Participante
class Participante(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='Email', unique=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes', verbose_name='Evento')
    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscrição')

    def __str__(self):
        return f'{self.nome} - {self.evento.nome}'
