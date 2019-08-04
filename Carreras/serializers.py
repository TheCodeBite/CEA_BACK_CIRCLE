from rest_framework import routers, serializers, viewsets
from Carreras.models import Carreras

class CarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = ('__all__')