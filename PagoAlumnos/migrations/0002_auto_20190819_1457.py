# Generated by Django 2.1.5 on 2019-08-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagoAlumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagoalumnos',
            name='costo',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagoalumnos',
            name='restante',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]