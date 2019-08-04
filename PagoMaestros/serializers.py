from rest_framework import routers, serializers, viewsets
from PagoMaestros.models import PagoMaestros

class PagoMaestrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = PagoMaestros
        fields = ('__all__')