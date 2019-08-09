from django.shortcuts import render
#======================= MODELOS ===============================
from Maestros.models import Maestros
#======================= Serializers =================================
from Maestros.serializers import MaestrosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class MaestrosList(APIView):
    def get(self, request, format=None):
        queryset= Maestros.objects.all()
        serializer = MaestrosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = MaestrosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class MaestrosDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Maestros.objects.get(pk=pk)
        serializer = MaestrosSerializers(queryset)
        return Response(serializer.data)

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profile = Maestros.objects.get(pk=pk)
        serializer = MaestrosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)