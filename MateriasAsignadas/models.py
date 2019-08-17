from django.db import models
from Maestros.models import Maestros
from Materias.models import Materias
# Create your models here.

class MateriasAsignadas(models.Model):
    inicio_modulo=models.DateField(null=False)
    fin_modulo=models.DateField(null=False)
    maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)
    horas_semanales = models.IntegerField(null=False)
    pagado=models.BooleanField(default=False,null=False)

    class Meta:
        db_table= "MateriasAsignadas"