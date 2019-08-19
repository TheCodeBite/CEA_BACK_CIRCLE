from django.db import models
from Alumnos.models import Alumnos
from MateriasAsignadas.models import MateriasAsignadas
# Create your models here.

class Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    materia_asignada = models.ForeignKey(MateriasAsignadas, on_delete=models.CASCADE)
    calificacion = models.FloatField(null=False)
    class Meta:
        db_table= "Calificaciones"