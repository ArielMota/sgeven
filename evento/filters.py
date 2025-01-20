from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from evento.models import Evento, Participante

class EventoFilterClass(AutoRQLFilterClass):
    MODEL = Evento

class ParticipanteFilterClass(AutoRQLFilterClass):
    MODEL = Participante
    FILTERS = [
    {
    'filter': 'evento',
    'source': 'evento__id',
    },
 
    ]