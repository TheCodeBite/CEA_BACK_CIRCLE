from rest_framework import routers, serializers, viewsets
from Calificaciones.models import Calificaciones

class CalificacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calificaciones
        fields = ('__all__')