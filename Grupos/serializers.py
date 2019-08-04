from rest_framework import routers, serializers, viewsets
from Grupos.models import Grupos

class GruposSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = ('__all__')