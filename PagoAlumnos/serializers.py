from rest_framework import routers, serializers, viewsets
from PagoAlumnos.models import PagoAlumnos

class PagoAlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = PagoAlumnos
        fields = ('__all__')