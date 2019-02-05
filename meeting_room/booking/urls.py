from django.conf.urls import url, include
from rest_framework import routers
#from booking.views import AgendamentoRudView, AgendamentoAPIView
##from booking.views import Sala_de_reuniaoRudView, Sala_de_reuniaoAPIView
from booking.views import Sala_de_reuniaoViewSet, AgendamentoViewSet

router = routers.DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'salas', Sala_de_reuniaoViewSet)


urlpatterns = [
       # url(r'^salas/$', Sala_de_reuniaoAPIView.as_view(), name='list_sala'),
       # url(r'^salas/(?P<id>\d+)/$', Sala_de_reuniaoRudView.as_view(), name='rud_sala'),
       # url(r'^agendamentos/$', AgendamentoAPIView.as_view(), name='url_agendamento'),
       # url(r'^agendamentos/(?P<id>\d+)/$', AgendamentoRudView.as_view(), name='url_agendamento'),
       url(r'^', include(router.urls)),
]
