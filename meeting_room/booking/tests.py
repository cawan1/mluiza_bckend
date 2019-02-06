from django.test import TestCase
from django.urls import reverse 
from rest_framework import status 
from rest_framework.test import APITestCase
from booking.models import Sala, Agendamento
from rest_framework.test import APIRequestFactory
from datetime import datetime


class SalaAPITestCase(APITestCase):

    def test_create_room(self):
        """
        Teste criação de uma sala
        """
        url = reverse('sala-list')
        data = {'nome' : 'Verde'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sala.objects.count(), 1)
        self.assertEqual(Sala.objects.get().nome, 'Verde')
        self.assertEqual(Sala.objects.get().id, 1)

    def test_update_room(self):
        """
        Teste alteracao de uma sala
        """
        url = reverse('sala-list')
        data = {'nome' : 'Amarela'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Sala.objects.get().nome, 'Amarela')
        self.assertEqual(Sala.objects.count(), 1)
        response = self.client.get('/api/salas/1/')
        #self.assertEqual(response.data, {'nome' : 'Amarela'})
        self.assertEqual(response.data, {'id': 1, 'nome': 'Amarela'})
        url = '/api/salas/1/'
        data_update = {'nome' : 'Vermelha'}
        response = self.client.put(url, data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Sala.objects.get().nome, 'Vermelha')
        self.assertEqual(Sala.objects.count(), 1)

    def test_delete_room(self):
        """
        Teste criação e delete de uma sala
        """
        url = reverse('sala-list')
        data = {'nome' : 'Verde'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sala.objects.count(), 1)
        self.assertEqual(Sala.objects.get().nome, 'Verde')
        self.assertEqual(Sala.objects.get().id, 1)
        url = '/api/salas/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class AgendamentoAPITestCase(APITestCase):
    def setUp(self):
        sala = Sala(nome="Verde")
        sala.save()

    def test_create_booking(self):
        """
        Teste criação de um agendamento
        """

        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00Z",
                "fim_reserva": "2019-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)

    def test_update_booking(self):
        """
        Teste alteracao de um agendamento
        """
        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_deOntem",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00",
                "fim_reserva": "2019-02-10T01:00:00"
                }
        response = self.client.post(url, data, format='json')
        response = self.client.get('/api/agendamentos/1/')
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_deOntem')
        url = '/api/agendamentos/1/'
        data_update = {"titulo": "Reuniao_deOntem",
                "sala": 1,
                "inicio_reserva": "2019-02-10T02:30:00",
                "fim_reserva": "2019-02-10T03:00:00"
                }
        response = self.client.put(url, data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(Agendamento.objects.get().inicio_reserva), str(datetime(2019, 2, 10, 2, 30)) + '+00:00')
        self.assertEqual(Agendamento.objects.count(), 1)


    def test_delete_booking(self):
        """
        Teste delete de um agendamento
        """
        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00Z",
                "fim_reserva": "2019-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)
        url = '/api/agendamentos/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_criar_agendamento_duplicado(self):
        """
        Teste Criar agendamento duplicado
        """
        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00Z",
                "fim_reserva": "2019-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)

        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00Z",
                "fim_reserva": "2019-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)
        
    def test_criar_agendamento_horario_conflitante(self):
        """
        Teste Criar agendamento horario conflitante
        """
        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:00:00Z",
                "fim_reserva": "2019-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)

        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_2",
                "sala": 1,
                "inicio_reserva": "2019-02-10T00:30:00Z",
                "fim_reserva": "2019-02-10T01:30:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Agendamento.objects.count(), 1)
        self.assertEqual(Agendamento.objects.get().titulo, 'Reuniao_1')
        self.assertEqual(Agendamento.objects.get().id, 1)

    def test_create_booking_past_date(self):
        """
        Teste criação de um agendamento
        """

        url = reverse('agendamento-list')
        data = {"titulo": "Reuniao_1",
                "sala": 1,
                "inicio_reserva": "2018-02-10T00:00:00Z",
                "fim_reserva": "2018-02-10T01:00:00Z"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Agendamento.objects.count(), 0)
