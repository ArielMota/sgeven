from django.db import models
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Cria automaticamente um usuário admin após as migrações'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = '123456'  # Defina uma senha segura
        email = 'admin@gmail.com'  # Email do usuário admin

        # Verifique se o usuário admin já existe
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.WARNING(f'O usuário {username} já existe.'))
        except ObjectDoesNotExist:
            # Crie o usuário admin se não existir
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Usuário admin "{username}" criado com suc

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
