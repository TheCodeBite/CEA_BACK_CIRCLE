from django.db import models
from Maestros.models import Maestros
# Create your models here.

class PagoMaestros(models.Model):
    maestro = models.ForeignKey(Maestros, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    pago = models.FloatField(null=False)
    class Meta:
        db_table= "PagoMaestros"