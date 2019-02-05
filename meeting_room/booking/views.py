from django.shortcuts import render

from rest_framework import (
        viewsets,
        generics,
        mixins,
        filters
        )

from booking.models import (
        Agendamento,
        Sala_de_reuniao
        )

from booking.serializers import (
        Sala_de_reuniaoSerializer,
        AgendamentoSerializer,
        )

# ViewSets define the view behavior.
class Sala_de_reuniaoViewSet(viewsets.ModelViewSet):
    queryset = Sala_de_reuniao.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    serializer_class = Sala_de_reuniaoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['sala__nome', 'inicio_reserva', 'fim_reserva']
    ordering_fields = '__all__'
    serializer_class = AgendamentoSerializer

