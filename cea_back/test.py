from django.shortcuts import render
#======================= MODELOS ===============================
from Carreras.models import Carreras
#======================= Serializers =================================
from Carreras.serializers import CarrerasSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class CarrerasList(APIView):
    def get(self, request, format=None):
        queryset= Carreras.objects.all()
        serializer = CarrerasSerializers(queryset,many=True)
        return Response(serializer.data)