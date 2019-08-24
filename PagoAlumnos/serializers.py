from rest_framework import routers, serializers, viewsets
from PagoAlumnos.models import PagoAlumnos

class PagoAlumnosSerializers(serializers.ModelSerializer):
    nombre_alumno = serializers.ReadOnlyField(source='alumno.nombre')
    apellidoP_alumno = serializers.ReadOnlyField(source='alumno.apellidopaterno')
    apellidoA_alumno = serializers.ReadOnlyField(source='alumno.apellidomaterno')
    class Meta:
        model = PagoAlumnos
        fields = ('__all__')