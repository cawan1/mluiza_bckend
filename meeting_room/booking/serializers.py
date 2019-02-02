from django.conf.urls import url, include
from rest_framework import serializers
from .models import Agendamento, Sala_de_reuniao 

# Serializers define the API representation.
class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ('id', 'titulo', 'sala', 'inicio_reserva', 'fim_reserva' )

class Sala_de_reuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala_de_reuniao
        fields = ('id', 'nome')
