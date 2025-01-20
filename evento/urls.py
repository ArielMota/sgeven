from django.urls import path, include
from rest_framework.routers import DefaultRouter
from evento.views import EventoModelViewSet, ParticipanteModelViewSet

router = DefaultRouter()
router.register('eventos', EventoModelViewSet)
router.register('participantes', ParticipanteModelViewSet)
urlpatterns = [
path('', include(router.urls)),
]