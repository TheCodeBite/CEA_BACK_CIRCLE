from rest_framework import routers, serializers, viewsets
from MateriasAsignadas.models import MateriasAsignadas

class MateriasAsignadasSerializers(serializers.ModelSerializer):
    class Meta:
        model = MateriasAsignadas
        fields = ('__all__')