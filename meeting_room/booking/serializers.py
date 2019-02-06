from django.conf.urls import url, include
from rest_framework import serializers
from booking.models import Agendamento, Sala 
from datetime import datetime
#import pytz
import logging

logger = logging.getLogger(__name__)

# Serializers define the API representation.
class AgendamentoSerializer(serializers.ModelSerializer):
    inicio_reserva = serializers.DateTimeField()
    fim_reserva  = serializers.DateTimeField()

    class Meta:
        model = Agendamento
        fields = ['id', 'titulo', 'sala', 'inicio_reserva', 'fim_reserva']


    def validate(self, data):
        """
        Check that start is before finish.
        Check if room is already booked
        """

        if data['inicio_reserva'] >= data['fim_reserva']:
            logger.error("Inicio da Reverva igual ou mais tarde ao Fim da reserva")
            raise serializers.ValidationError("Inicio da Reverva igual ou mais tarde ao Fim da reserva")


        # Busca agendamentos por sala com inicio entre:  o inicio da reserva   e  o  fim da reserva
        busca_periodo_inicio = Agendamento.objects.filter(sala__exact=data['sala']).filter(inicio_reserva__gte=data['inicio_reserva']).filter(inicio_reserva__lt=data['fim_reserva'])
        busca_periodo_fim = Agendamento.objects.filter(sala__exact=data['sala']).filter(fim_reserva__gt=data['inicio_reserva']).filter(fim_reserva__lte=data['fim_reserva'])
        if busca_periodo_inicio or busca_periodo_fim :
            logger.error("Já existe reserva para a sala no horario requisitado")
            raise serializers.ValidationError("Já existe reserva para a sala no horario requisitado")


        now = datetime.now()
        #utc=pytz.UTC

        #if data['inicio_reserva'] < utc.localize(now) or data['fim_reserva'] < utc.localize(now):
        if data['inicio_reserva'] < now or data['fim_reserva'] < now :
            logger.error("Nao e possivel agendar no passado, o que passou, passou")
            raise serializers.ValidationError("Nao e possivel agendar no passado, o que passou, passou")

        return data


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id' , 'nome']
