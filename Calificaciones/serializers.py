from rest_framework import routers, serializers, viewsets
from Calificaciones.models import Calificaciones

class CalificacionesSerializers(serializers.ModelSerializer):
    matricula = serializers.ReadOnlyField(source='alumno.matricula')
    nombre = serializers.ReadOnlyField(source='alumno.nombre')
    apellidoP = serializers.ReadOnlyField(source='alumno.apellidopaterno')
    apellidoM = serializers.ReadOnlyField(source='alumno.apellidomaterno')
    class Meta:
        model = Calificaciones
        fields = ('__all__')