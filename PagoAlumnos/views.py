from django.shortcuts import render
#======================= MODELOS ===============================
from PagoAlumnos.models import PagoAlumnos
#======================= Serializers =================================
from PagoAlumnos.serializers import PagoAlumnosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class PagoAlumnosList(APIView):
    def get(self, request, format=None):
        queryset= PagoAlumnos.objects.all()
        serializer = PagoAlumnosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = PagoAlumnosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class PagoAlumnosDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= PagoAlumnos.objects.get(pk=pk)
        serializer = PagoAlumnosSerializers(queryset)
        return Response(serializer.data)

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = PagoAlumnos.objects.get(pk=pk)
        serializer = PagoAlumnosSerializers(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)