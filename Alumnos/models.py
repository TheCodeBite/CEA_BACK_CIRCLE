from django.db import models
from Carreras.models import Carreras
from Grupos.models import Grupos
# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    apellidopaterno=models.CharField(max_length=50,null=False)
    apellidomaterno=models.CharField(max_length=50,null=False)
    matricula = models.CharField(max_length=15,null=False, unique=True)
    curp = models.CharField(max_length=20,null=False, unique=True)
    carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE,null=True) #solo universitarios
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20,null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=20,null=False)
    fechadenacimiento = models.DateField(null=False)
    folio_certificado = models.CharField(max_length=30,null=False)
    direccion = models.TextField(null=False)
    municipio = models.TextField(null=False)
    modalidad = models.CharField(max_length=30,null=False)
    telefono = models.CharField(max_length=11,null=False)
    tutor = models.CharField(max_length=150,null=True) #Solo prepa
    certificado_original = models.IntegerField(null=False) #0 = No y 1=Si
    certificado_tres_copias = models.IntegerField(null=False)
    acta_nacimiento = models.IntegerField(null=False)
    acta_de_nacimiento_tres_copias = models.IntegerField(null=False)
    ine_tres_copias = models.IntegerField(null=False)
    comprobante_de_domicilio = models.IntegerField(null=False)
    tipo = models.CharField(max_length=30,null=False)
    class Meta:
        db_table= "Alumnos"