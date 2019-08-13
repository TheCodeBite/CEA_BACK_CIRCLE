from django.db import models
# Create your models here.

class Grupos(models.Model):
    nombre = models.CharField(max_length=150,null=False, unique=True)
    modalidad = models.CharField(max_length=20,null=False)
    class Meta:
        db_table= "Grupos"