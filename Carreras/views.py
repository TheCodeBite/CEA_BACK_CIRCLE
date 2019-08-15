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
    
    def post (self, request, format=None):
        serializer = CarrerasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class CarrerasDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Carreras.objects.get(pk=pk)
        serializer = CarrerasSerializers(queryset)
        return Response(serializer.data)
    
    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        carrera = Carreras.objects.get(pk=pk)
        serializer = CarrerasSerializers(carrera,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)