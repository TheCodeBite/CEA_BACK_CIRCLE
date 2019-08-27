from django.shortcuts import render
#======================= MODELOS ===============================
from Calificaciones.models import Calificaciones
#======================= Serializers =================================
from Calificaciones.serializers import CalificacionesSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class CalificacionesList(APIView):
    def get(self, request, format=None):
        queryset= Calificaciones.objects.all()
        serializer = CalificacionesSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = CalificacionesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class CalificacionesDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Calificaciones.objects.filter(materia_asignada=pk).order_by('alumno__apellidopaterno')
        serializer = CalificacionesSerializers(queryset,many=True)
        return Response(serializer.data)
        
    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        calificacion = Calificaciones.objects.get(pk=pk)
        serializer = CalificacionesSerializers(calificacion,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)