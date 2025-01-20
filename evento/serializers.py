from rest_framework import serializers
from evento.models import Evento, Participante, User


class EventoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class UsuarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']  # Ajuste os campos conforme necessário


class ParticipanteModelSerializer(serializers.ModelSerializer):
    #evento = EventoModelSerializer()  # Serializa o campo 'evento' com o EventoModelSerializer
    #usuario = UsuarioModelSerializer()  # Serializa o campo 'usuario' com o UsuarioModelSerializer

    class Meta:
        model = Participante
        fields = '__all__'