from django.shortcuts import render
#======================= MODELOS ===============================
from PagoMaestros.models import PagoMaestros
#======================= Serializers =================================
from PagoMaestros.serializers import PagoMaestrosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class PagoMaestrosList(APIView):
    def get(self, request, format=None):
        queryset= PagoMaestros.objects.all()
        serializer = PagoMaestrosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = PagoMaestrosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class PagoMaestrosDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= PagoMaestros.objects.get(pk=pk)
        serializer = PagoMaestrosSerializers(queryset)
        return Response(serializer.data)

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = PagoMaestros.objects.get(pk=pk)
        serializer = PagoMaestrosSerializers(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)