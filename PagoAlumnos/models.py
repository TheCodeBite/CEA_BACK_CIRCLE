from django.db import models
from Alumnos.models import Alumnos
# Create your models here.

class PagoAlumnos(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    pago = models.FloatField(null=False)
    tipo =  models.CharField(max_length=100,null=False)
    class Meta:
        db_table= "PagoAlumnos"