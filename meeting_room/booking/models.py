from django.db import models

class Sala_de_reuniao(models.Model):
    nome = models.CharField(max_length=32, null=False)
    def reservar(titulo, self, inicio_reserva, fim_reserva):
        Agendamento(titulo, self, inicio_reserva, fim_reserva).save()


class Agendamento(models.Model):
    titulo = models.CharField(max_length=144, null=False)
    sala = models.ForeignKey(Sala_de_reuniao, on_delete=models.CASCADE , related_name='agendamentos')
    inicio_reserva = models.DateTimeField()
    fim_reserva = models.DateTimeField()




# Create your models here.
