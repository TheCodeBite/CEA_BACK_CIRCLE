from django.shortcuts import render
#======================= MODELOS ===============================
from MateriasAsignadas.models import MateriasAsignadas
#======================= Serializers =================================
from MateriasAsignadas.serializers import MateriasAsignadasSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class MateriasAsignadasList(APIView):
    def get(self, request, format=None):
        queryset= MateriasAsignadas.objects.all()
        serializer = MateriasAsignadasSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = MateriasAsignadasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class MateriasAsignadasDetails(APIView):
    def get (self, request,*args, **kwargs):
        maestro = kwargs.get('maestro')
        queryset= MateriasAsignadas.objects.all()
        queryset= queryset.filter(maestro=maestro)
        queryset = queryset.filter(pagado = False)
        serializer = MateriasAsignadasSerializers(queryset,many=True)
        return Response(serializer.data)

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('maestro')
        materiasAsignada = MateriasAsignadas.objects.get(pk=pk)
        serializer = MateriasAsignadasSerializers(materiasAsignada,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)