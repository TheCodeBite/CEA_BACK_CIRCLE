from rest_framework import routers, serializers, viewsets
from Materias.models import Materias

class MateriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = ('__all__')