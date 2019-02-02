from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento, Sala_de_reuniao
from .serializers import Sala_de_reuniaoSerializer, AgendamentoSerializer

# ViewSets define the view behavior.
class Sala_de_reuniaoViewSet(viewsets.ModelViewSet):
    queryset = Sala_de_reuniao.objects.all()
    serializer_class = Sala_de_reuniaoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
# Create your views here.
