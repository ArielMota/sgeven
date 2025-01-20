from django.contrib import admin
from .models import Evento, Participante

# Modelo de Evento
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'organizador', 'data_inicio', 'data_fim', 'local')  # Campos que aparecem na lista
    list_filter = ('organizador', 'data_inicio', 'data_fim')  # Filtros laterais
    search_fields = ('nome', 'descricao')  # Campos para busca
    ordering = ('-data_inicio',)  # Ordenação por data de início

# Modelo de Participante
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'data_inscricao')  # Campos que aparecem na lista
    list_filter = ( 'evento',)  # Filtros laterais
    search_fields = ( 'evento__nome',)  # Busca por nome de usuário e evento
    raw_id_fields = ( 'evento',)  # Usa IDs ao invés de caixas de seleção para melhorar performance
    ordering = ('-data_inscricao',)  # Ordenação pela data de inscrição

# Registrando os modelos com suas respectivas configurações
admin.site.register(Evento, EventoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
