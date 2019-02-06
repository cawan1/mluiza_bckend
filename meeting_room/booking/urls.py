from django.conf.urls import url, include
from rest_framework import routers
#from booking.views import AgendamentoRudView, AgendamentoAPIView
##from booking.views import SalaRudView, SalaAPIView
from booking.views import SalaViewSet, AgendamentoViewSet

router = routers.DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'salas', SalaViewSet)


urlpatterns = [
       # url(r'^salas/$', SalaAPIView.as_view(), name='list_sala'),
       # url(r'^salas/(?P<id>\d+)/$', SalaRudView.as_view(), name='rud_sala'),
       # url(r'^agendamentos/$', AgendamentoAPIView.as_view(), name='url_agendamento'),
       # url(r'^agendamentos/(?P<id>\d+)/$', AgendamentoRudView.as_view(), name='url_agendamento'),
       url(r'^', include(router.urls)),
]
