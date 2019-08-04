from django.shortcuts import render
#======================= MODELOS ===============================
from Materias.models import Materias
#======================= Serializers =================================
from Materias.serializers import MateriasSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class MateriasList(APIView):
    def get(self, request, format=None):
        queryset= Materias.objects.all()
        serializer = MateriasSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = MateriasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class MateriasDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Materias.objects.get(pk=pk)
        serializer = MateriasSerializers(queryset)
        return Response(serializer.data)