from django.db import models


class Agendamento(models.Model):
    titulo = models.CharField(max_length=144, null=False)
    sala = models.ForeginKey(Sala_de_reuniao, related_name='agendamentos')
    inicio_reserva = models.DateField()
    fim_resersa = models.DateField()


class Sala_de_reuniao(models.Model):
    nome = models.CharField(max_length=32, null=False)

    def reservar(titulo, self, inicio_reserva, fim_reserva):
        Agendamento(titulo, self, inicio_reserva, fim_reserva).save()


# Create your models here.
