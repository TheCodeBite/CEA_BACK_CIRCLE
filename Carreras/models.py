from django.db import models
# Create your models here.

class Carreras(models.Model):
    nombre = models.CharField(max_length=100,null=False, unique=True)
    nomenclatura = models.CharField(max_length=15,null=False, unique=True)

    class Meta:
        db_table= "Carreras"