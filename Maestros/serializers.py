from rest_framework import routers, serializers, viewsets
from Maestros.models import Maestros

class MaestrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maestros
        fields = ('__all__')