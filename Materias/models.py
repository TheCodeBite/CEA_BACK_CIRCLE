from django.db import models
from Carreras.models import Carreras
# Create your models here.

class Materias(models.Model):
    nombre = models.CharField(max_length=150,null=False, unique=True)
    carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    semestre = models.IntegerField(null=False)
    class Meta:
        db_table= "Materias"