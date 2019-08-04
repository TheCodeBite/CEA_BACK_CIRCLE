from django.shortcuts import render
#======================= MODELOS ===============================
from Grupos.models import Grupos
#======================= Serializers =================================
from Grupos.serializers import GruposSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class GruposList(APIView):
    def get(self, request, format=None):
        queryset= Grupos.objects.all()
        serializer = GruposSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = GruposSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class GruposDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Grupos.objects.get(pk=pk)
        serializer = GruposSerializers(queryset)
        return Response(serializer.data)