from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=32, null=False)
    #kdef reservar(titulo, self, inicio_reserva, fim_reserva):
     #   Agendamento(titulo, self, inicio_reserva, fim_reserva).save()

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    titulo = models.CharField(max_length=144, null=False)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE , related_name='agendamentos')
    inicio_reserva = models.DateTimeField()
    fim_reserva = models.DateTimeField()

    def __str__(self):
        return self.titulo




# Create your models here.
