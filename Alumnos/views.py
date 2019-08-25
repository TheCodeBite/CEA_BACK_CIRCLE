from django.shortcuts import render
#======================= MODELOS ===============================
from Alumnos.models import Alumnos
#======================= Serializers =================================
from Alumnos.serializers import AlumnosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class AlumnosList(APIView):
    def get(self, request, format=None):
        queryset= Alumnos.objects.all()
        serializer = AlumnosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = AlumnosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class AlumnosDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Alumnos.objects.get(pk=pk)
        serializer = AlumnosSerializers(queryset)
        return Response(serializer.data)

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        alumno = Alumnos.objects.get(pk=pk)
        serializer = AlumnosSerializers(alumno,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumnosEstado(APIView):
    def get(self, request,*args, **kwargs):
        estado = kwargs.get('pk')
        queryset= Alumnos.objects.filter(estado=estado)
        serializer = AlumnosSerializers(queryset,many=True)
        return Response(serializer.data)