from rest_framework import routers, serializers, viewsets
from Alumnos.models import Alumnos

class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('__all__')