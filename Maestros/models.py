from django.db import models
# Create your models here.

class Maestros(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    apellidopaterno = models.CharField(max_length=50,null=False)
    apellidomaterno = models.CharField(max_length=50,null=False)
    tituloprofesional= models.CharField(max_length=150,null=False)
    cedulaprofesional = models.CharField(max_length=150,null=False,unique=True)
    institucioneducativa = models.CharField(max_length=200,null=False)
    telefono = models.CharField(max_length=11,null=False)
    direccion = models.TextField(null=False)
    sexo = models.CharField(max_length=10,null=False)
    edad = models.IntegerField(null=False)
    fechadenacimiento = models.DateField(null=False)
    correo = models.CharField(max_length=150,null=False)
    tipo = models.CharField(max_length=150,null=False)
    estado = models.CharField(max_length=150,null=False)

    class Meta:
        db_table= "Maestros"