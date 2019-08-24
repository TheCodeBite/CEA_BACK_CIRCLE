from rest_framework import routers, serializers, viewsets
from MateriasAsignadas.models import MateriasAsignadas

class MateriasAsignadasSerializers(serializers.ModelSerializer):
    nombre_maestro = serializers.ReadOnlyField(source='maestro.nombre')
    nombre_materia = serializers.ReadOnlyField(source='materia.nombre')
    class Meta:
        model = MateriasAsignadas
        fields = ('__all__')