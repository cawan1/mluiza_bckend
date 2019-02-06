from django.shortcuts import render

from rest_framework import (
        viewsets,
        generics,
        mixins,
        filters
        )

from booking.models import (
        Agendamento,
        Sala
        )

from booking.serializers import (
        SalaSerializer,
        AgendamentoSerializer,
        )

# ViewSets define the view behavior.
class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id' , 'nome']
    serializer_class = SalaSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['sala__nome', 'inicio_reserva', 'fim_reserva']
    ordering_fields = '__all__'
    serializer_class = AgendamentoSerializer

